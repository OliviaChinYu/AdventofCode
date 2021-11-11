import os
import html
import numpy as np

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'), 'r')


def part_one():
	lit_count = 0
	mem_count = 0
	for line in f:
		line = line.replace('\n','')
		lit_count = lit_count + len(line)
		mem = line[1:-1]
		i = 0
		while i < len(mem)-1:
			if mem[i]+mem[i+1] == r'\\' or mem[i]+mem[i+1] == r'\"':
				mem = mem[:i]+mem[i+1:]
			elif mem[i]+mem[i+1] == r'\x':
				mem = mem[:i]+mem[i+3:]
			else:
				pass
			i = i + 1
		mem_count = mem_count + len(mem)

	total = lit_count - mem_count
	return total

def part_two():
	lit_count = 0
	new_count = 0
	for line in f:
		line = line.replace('\n','')
		lit_count = lit_count + len(line)
		new_len = len(line)
		for l in line:
			if l in ['\\','\"']:
				new_len += 1
		new_len = new_len + 2
		new_count = new_count + new_len

	total = new_count - lit_count
	return total


print(part_one())