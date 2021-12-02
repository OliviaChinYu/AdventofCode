import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'), 'r')

def part_one():
	x = []
	y = []

	for line in f:
		command = line.split()
		if 'forward' in command:
			x.append(int(command[1]))
		elif 'down' in command:
			y.append(int(command[1]))
		else:
			y.append(int(command[1])*-1)

	x_sum = sum(x)
	y_sum = sum(y)

	final_depth = x_sum * y_sum
	return final_depth


def part_two():
	x = []
	y = []
	aim = []

	for line in f:
		command = line.split()
		if 'down' in command:
			aim.append(int(command[1]))
		elif 'up' in command:
			aim.append(int(command[1])*-1)
		else:
			aim_sum = sum(aim)
			x.append(int(command[1]))
			y.append(int(command[1])*aim_sum)

	x_sum = sum(x)
	y_sum = sum(y)

	final_depth = x_sum * y_sum
	return final_depth

print(part_two())