import os 
import re

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'), 'r')

def part_one():
	nice = 0
	for line in f:
		vowel = 0
		prev = ''
		current = ''
		badstrings = False
		cond3 = False
		for l in line:
			prev = current
			current = l
			if l in ['a','e','i','o','u']:
				vowel += 1
			if prev + current in ['ab', 'cd', 'pq', 'xy']:
				badstrings = True
			if prev == current:
				cond3 = True
		cond1 = vowel > 2
		cond2 = badstrings is False
		if cond1 and cond2 and cond3:
			nice += 1
	return nice

def part_two():
	nice = 0
	for line in f:
		superprev = ''
		prevprev = ''
		prev = ''
		current = ''
		dbl_list = []
		cond1 = False 		# a pair of letters appears twice
		# cond2 = True		# the pair of letters cannot overlap
		cond3 = False		# sandwiched letters
		for l in line:
			superprev = prevprev
			prevprev = prev
			prev = current
			current = l
			if len(prevprev+prev) == 2:
				dbl_list.append(prevprev+prev)

			pair = False
			overlap = False

			if prev+current in dbl_list:
				pair = True
			if prevprev+prev == prev+current:
				overlap = True
			if superprev+prevprev == prev+current:
				overlap = False
			if pair is True and overlap is False:
				cond1 = True
			if prevprev == current:
				cond3 = True
		if cond1 and cond3:
			nice += 1
	return nice

print(part_two())