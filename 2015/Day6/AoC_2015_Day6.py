import pandas as pd
import numpy as np
import os
import sys

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'), 'r')

lst = []
for i in range(15):
	lst.append(0)

df = pd.DataFrame()
inc = 0

for i in range(15):
	df[inc] = np.array(lst)
	inc = inc + 1


for line in f:
	instruc = line.replace(' ',',')
	instruc = instruc.replace('\n','')
	instr_list = instruc.split(',')
	print(instr_list)
	row_start = int(instr_list[-5]) # min x height
	row_end = int(instr_list[-2]) # max x height
	col_start = int(instr_list[-4]) # min y w
	col_end = int(instr_list[-1]) # max y w
	if 'on' in instr_list:
		df.loc[row_start:row_end, col_start:col_end] = 1
	elif 'off' in instr_list:
		df.loc[row_start:row_end, col_start:col_end] = 0
	elif 'toggle' in instr_list:
		df.loc[row_start:row_end, col_start:col_end] = df.loc[row_start:row_end, col_start:col_end] == 0 if 1 else 0	
	else:
		pass

print(df.values.sum())