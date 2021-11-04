import os
import html
import numpy as np

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'), 'r')
# esc = html.unescape(mem)


def part_one():
	lit_count = 0
	mem_count = 0
	for line in f:
		print(line)
		line = line.replace('\n','')
		lit_count = lit_count + len(line)
		print(len(line))
		mem = line[1:-1]
		mem_len = len(mem)
		i = 0
		while i < mem_len-1:
			if mem[i]+mem[i+1] == r'\\' or mem[i]+mem[i+1] == r'\"':
				mem_len = mem_len - 1
			i = i + 1
		print(mem_len)


	total = lit_count - mem_count
	return total


print(part_one())