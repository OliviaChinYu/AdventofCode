import pandas as pd
import numpy as np
import os
import sys

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'), 'r')

lst = []
size = 1000
for i in range(size):
	new = []
	for j in range(size):
		new.append(0)
	lst.append(new)

for line in f:
	instruc = line.replace(' ',',')
	instruc = instruc.replace('\n','')
	instr_list = instruc.split(',')
	# print(instr_list)
	row_start = int(instr_list[-5]) # min x height
	row_end = int(instr_list[-2]) # max x height
	col_start = int(instr_list[-4]) # min y w
	col_end = int(instr_list[-1]) # max y w

	for rowIndex in range(row_start, row_end+1):
		for colIndex in range(col_start, col_end+1):
			if 'on' in line:
				lst[rowIndex][colIndex] = 1
			elif 'off' in line: 
				lst[rowIndex][colIndex] = 0
			else:
				lst[rowIndex][colIndex] = lst[rowIndex][colIndex] == 0 if 1 else 0
				

result = 0
for i in range(size):
	for j in range(size):
		result = result + lst[i][j]

print(result)


# df = pd.DataFrame()
# inc = 0
# for i in range(10):
# 	df[inc] = np.array(lst)
# 	inc = inc + 1


# # for line in f:
# # 	instruc = line.replace(' ',',')
# # 	instruc = instruc.replace('\n','')
# # 	instr_list = instruc.split(',')
# # 	# print(instr_list)
# # 	row_start = instr_list[-4]
# # 	row_end = instr_list[-1]
# # 	col_start = instr_list[-5]
# # 	col_end = instr_list[-2]
# # 	if 'on' in instr_list:
# # 		df.loc[row_start:row_end, col_start:col_end] = 1
# # 	elif 'off' in instr_list:
# # 		df.loc[row_start:row_end, col_start:col_end] = -1
# # 	elif 'toggle' in instr_list:
# # 		df.loc[row_start:row_end, col_start:col_end] = df.loc[row_start:row_end, col_start:col_end]*-1	
# # 	else:
# # 		pass

# df.loc[1:4, 1:4] = 1
# df.loc[2:5, 2:5] = df.loc[2:5, 2:5]*-1

# print(df)
# df = df.mask(df < 0, 0)
# # print(df)

# print(df.values.sum())