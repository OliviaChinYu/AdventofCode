import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'), 'r')

def part_one():
	count = 0
	prev = 0

	for depth in f:
		if int(depth) > prev:
			count += 1
		prev = int(depth)

	answer = count - 1
	return answer

def part_two():
	input_list = []
	for depth in f:
		input_list.append(int(depth))

	depth_list = []
	prevprev = input_list[0]
	prev = input_list[1]
	last = len(input_list)
	for i in input_list[2:last]:
		trio_depth = prevprev + prev + i
		depth_list.append(trio_depth)
		prevprev = prev
		prev = i

	count = 0
	prev_depth = 0
	for depth in depth_list:
		if int(depth) > prev_depth:
			count += 1
		prev_depth = int(depth)

	answer = count - 1
	return answer



print(part_two())