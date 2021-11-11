import time

pinput = '3113322113'

def look_and_say(phrase):
	num = phrase[0]
	num_count = 0
	num_list = []
	for idx, val in enumerate(phrase):
		if val == num:
			num_count += 1
		else:
			num_list.append(str(num_count))
			num_list.append(num)
			num = val
			num_count = 1
	num_list.append(str(num_count))
	num_list.append(num)
	new_input = ''.join(num_list)
	return new_input

def las_iter(iter_count, pinput):
	for i in range(iter_count):
		print(i)
		look_and_say(pinput)
		pinput = look_and_say(pinput)

	print(len(pinput))

#Part one
start_time = time.time()
las_iter(50, pinput)
print("--- %s seconds ---" % (time.time() - start_time))
	



