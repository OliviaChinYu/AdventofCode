import hashlib

def plus_one():
	secret_key = 'iwrupvqb'
	inc = 346384
	answer = ''
	while answer[:5] != '000000':
		print(inc)
		inc = inc + 1
		inc_string = str(inc)
		hash_string = secret_key + inc_string
		result = hashlib.md5(hash_string.encode())
		answer = result.hexdigest()
		# print(answer)
	return inc



# print(plus_one())

