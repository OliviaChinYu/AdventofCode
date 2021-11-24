import copy
import os
import json
import time

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'), 'r')

puzzle_input = json.load(f)

class Recurse:
	def __init__(self, part):
		self.part = part
		self.numbers = []

	def dict_iter(self, dct):
		for key, value in dct.items():
			if self.part == 'parttwo':
				if 'red' in dct or 'red' in dct.values():
					return None
			if key is None or value is None:
				return None
			elif isinstance(key, int):
				self.numbers.append(key)
			elif isinstance(value, int):
				self.numbers.append(value)
			elif isinstance(value, dict):
				di = self.dict_iter(value)
				if di:
					for num in di:
						self.numbers.append(num)
			elif isinstance(value, list):
				li = self.list_iter(value)
				if li:
					for num in li:
						self.numbers.append(num)

	def list_iter(self, lst):
		for item in lst:
			if item is None:
				return None
			elif isinstance(item, int):
				self.numbers.append(item)
			elif isinstance(item, dict):
				di = self.dict_iter(item)
				if di:
					for num in di:
						self.numbers.append(num)
			elif isinstance(item, list):
				li = self.list_iter(item)
				if li:
					for num in li:
						self.numbers.append(num)


def part_one():
	start_time = time.time()
	re = Recurse('partone')
	total = 0
	re.list_iter(puzzle_input)
	for number in re.numbers:
		total += number
	print("--- %s seconds ---" % (time.time() - start_time))
	return(total)

def part_two():
	start_time = time.time()
	re = Recurse('parttwo')
	total = 0
	re.list_iter(puzzle_input)
	for number in re.numbers:
		total += number
	print("--- %s seconds ---" % (time.time() - start_time))
	return(total)

print(part_one())
print(part_two())
