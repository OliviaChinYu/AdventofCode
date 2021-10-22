"""AoC_2015_Day3"""
import os
import numpy as np

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'), 'r')


directions = f.read()

# directions = '^v>>>>^^^<v'

santa_list = []
robo_list = []
santa_coor = [0,0]
robo_coor = [0,0]
santa_list.append(tuple(santa_coor))

def santa_only():
	for d in directions:
		if d == '^':
			santa_coor[1] = santa_coor[1] + 1
		elif d == 'v':
			santa_coor[1] = santa_coor[1] - 1
		elif d == '>':
			santa_coor[0] = santa_coor[0] + 1
		elif d == '<':
			santa_coor[0] = santa_coor[0] - 1
		else:
			pass
		santa_tuple = tuple(santa_coor)
		santa_list.append(santa_tuple)
		
	santa_set = set(santa_list)
	unique_santa = list(santa_set)
	santa_len = len(unique_santa)
	return santa_len

def plus_robo_santa():
	for idx, d in enumerate(directions):
		if idx % 2 == 0:
			pass
		elif d == '^':
			santa_coor[1] = santa_coor[1] + 1
		elif d == 'v':
			santa_coor[1] = santa_coor[1] - 1
		elif d == '>':
			santa_coor[0] = santa_coor[0] + 1
		elif d == '<':
			santa_coor[0] = santa_coor[0] - 1
		else:
			pass
		santa_tuple = tuple(santa_coor)
		santa_list.append(santa_tuple)

	for idx, d in enumerate(directions):
		if idx % 2 != 0:
			pass
		elif d == '^':
			robo_coor[1] = robo_coor[1] + 1
		elif d == 'v':
			robo_coor[1] = robo_coor[1] - 1
		elif d == '>':
			robo_coor[0] = robo_coor[0] + 1
		elif d == '<':
			robo_coor[0] = robo_coor[0] - 1
		else:
			pass
		robo_tuple = tuple(robo_coor)
		robo_list.append(robo_tuple)

	all_coor = santa_list + robo_list
	list_set = set(all_coor)
	unique_list = list(list_set)
	unique_len = len(unique_list)

	return unique_len

print(plus_robo_santa())