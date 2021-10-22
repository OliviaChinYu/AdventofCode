import hashlib

secret_key = 'iwrupvqb'

def part_one():
	inc = 0
	answer = ''
	while answer[:5] != '00000':

		inc = inc + 1
		inc_string = str(inc)
		hash_string = secret_key + str(inc)
		result = hashlib.md5(hash_string.encode())
		answer = result.hexdigest()
	return inc

def part_two():
	inc = 0
	answer = ''
	while answer[:6] != '000000':

		inc = inc + 1
		inc_string = str(inc)
		hash_string = secret_key + str(inc)
		result = hashlib.md5(hash_string.encode())
		answer = result.hexdigest()
	return inc




print(part_two()())

