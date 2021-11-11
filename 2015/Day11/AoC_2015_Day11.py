import time

partone = 'hxbxwxba'
sample_input = 'hxbbcczz'
parttwo = 'hxbxxyzz'


input_list = list(parttwo)
idx = len(input_list)-1
cond1 = False
cond2 = True
cond3 = False

def letter_inc(idx):
	if input_list[idx] == 'z':
		nxt_idx = idx - 1
		input_list[idx] = 'a'
		letter_inc(nxt_idx)
	else:
		input_list[idx] = chr(ord(input_list[idx])+1)

def condition_1(input_list):
	for i in range(len(input_list)-2):
		first = input_list[i]
		second = input_list[i+1]
		third = input_list[i+2]
		cond1a = first == chr(ord(second)-1)
		cond1b = second == chr(ord(third)-1)
		cond1 = cond1a and cond1b is True
		if cond1 is True: break
	return cond1

def condition_2(input_list):
	cond2 = False if any(x in ['i','o', 'l'] for x in input_list) else True
	return cond2

def condition_3(input_list):
	dupe_count = []
	letter = input_list[0]
	count = 0
	for i in input_list:
		if i == letter:
			count += 1
		else: 
			letter = i
			count = 1
		if count == 2:
			dupe_count.append(letter)
	cond3 = len(dupe_count) > 1
	return cond3

def all_conditions(input_list):
	cond1 = False
	cond2 = True
	cond3 = False
	dbl_count = 0
	dbl_list = []
	letter = input_list[0]
	iter_count = 0
	for i in input_list[:6]:
		first = i
		second = input_list[iter_count+1]
		third = input_list[iter_count+2]
		cond1a = first == chr(ord(second)-1)
		cond1b = second == chr(ord(third)-1)
		if i == letter:
			dbl_count += 1
		else:
			letter = i
			dbl_count = 1
		if dbl_count == 2: dbl_list.append(letter)
		if cond1a and cond1b is True: cond1 = True
		if i in ['i','o', 'l']: cond2 = False
		iter_count += 1
	for i in input_list[6:]:
		if i == letter:
			dbl_count += 1
		else:
			letter = i
			dbl_count = 1
		if dbl_count == 2: dbl_list.append(letter)
	if len(dbl_list) > 1: cond3 = True
	return cond1, cond2, cond3



start_time = time.time()
while (cond1 and cond2 and cond3) is False:			# Looking for 3 True conditions to break While loop
# for i in range(28):
	letter_inc(idx)
	# print(input_list, cond1, cond2, cond3)
	# cond1 = condition_1(input_list)
	# cond2 = condition_2(input_list)
	# cond3 = condition_3(input_list)
	# cond1, cond2, cond3 = all_conditions(input_list)
	cond1, cond2, cond3 = all_conditions(input_list)


new_pw = ''.join(input_list)

print(new_pw)
print("--- %s seconds ---" % (time.time() - start_time))