"""AoC_2015_Day1.py"""

filepath = r'C:\Users\olivia.chin\source\repos\AdventofCode\2015\Day1\input.txt'

file1 = open(filepath, 'r')
instructions = file1.read()


def final_floor():
	floor = 0
	for i in instructions: 
		if i == '(': 
			floor = floor + 1
		elif i == ')':
			floor = floor - 1
		else:
			pass
	return floor

def basement_index():
	floor = 0
	for idx, val in enumerate(instructions): 
		print(idx, floor)
		if floor < 0:
			break
		elif val == '(': 
			floor = floor + 1
		elif val == ')':
			floor = floor - 1
		else:
			pass
	return idx, floor


print(basement_index())

