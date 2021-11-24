import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'), 'r')

seating_dict = {}
names = []
arrangements = []

def part_one():
	for line in f:
		inp_list = line.split()
		p1 = inp_list[0]
		p2 = inp_list[10].replace('.','')
		mood = 1 if inp_list[2] == 'gain' else -1
		amount = int(inp_list[3])
		happiness = mood*amount
		if p1 not in names:
			names.append(p1)
		if p1 in seating_dict:
			seating_dict[p1].append((p2, happiness))
		else: 
			seating_dict[p1] = [(p2, happiness)]

def part_two():
	for line in f:
		inp_list = line.split()
		p1 = inp_list[0]
		p2 = inp_list[10].replace('.','')
		mood = 1 if inp_list[2] == 'gain' else -1
		amount = int(inp_list[3])
		happiness = mood*amount
		if p1 not in names:
			names.append(p1)
		if p1 in seating_dict:
			seating_dict[p1].append((p2, happiness))
		else: 
			seating_dict[p1] = [(p2, happiness)]
			seating_dict[p1].append(('me',0))
	for n in names:
		if 'me' in seating_dict:
			seating_dict['me'].append((n,0))
		else: seating_dict['me'] = [(n, 0)]
	names.append('me')

def find_arrangement(key, arrangement=[]):
	option = arrangement + [key]
	if len(option) == len(names):
		return option
	for node, amt in seating_dict[key]:
		if node not in option:
			op = find_arrangement(node, option)
			if op:
				arrangements.append(op)

# part_one()
part_two()
find_arrangement(names[0])
totals = []
for option in arrangements:
	total = 0
	for i in range(len(option)):
		prev = i - 1
		nxt = i + 1 if i < len(option)-1 else 0
		for node, amt in seating_dict[option[i]]:
			if node == option[prev]:
				total += amt
			if node == option[nxt]:
				total += amt
	totals.append(total)

print(max(totals))

