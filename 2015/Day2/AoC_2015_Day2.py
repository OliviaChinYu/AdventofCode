"""AoC_2015_Day2"""
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'), 'r')


def wrapping_paper():
	total = 0
	for line in f:
		dimension = list(map(int, line.split('x')))
		dimension.sort()
		small = 3 * dimension[0] * dimension[1]
		med = 2 * dimension[0] * dimension[2]
		large = 2 * dimension[1] * dimension[2]
		sqfeet = small + med + large
		total = total + sqfeet
	return total

def ribbon():
	length = 0
	for line in f:
		dimension = list(map(int, line.split('x')))
		dimension.sort()
		wrap = (2 * dimension[0]) + (2 * dimension[1])
		bow = dimension[0] * dimension[1] * dimension[2]
		length = length + wrap + bow
	return length

print(ribbon())