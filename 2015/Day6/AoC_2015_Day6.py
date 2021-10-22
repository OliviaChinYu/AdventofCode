import pandas as pd
import numpy as np
import os
import sys

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'), 'r')

lst = []
for i in range(1000):
	lst.append(-1)

df = pd.DataFrame()
inc = 0
for i in range(1000):
	df[inc] = np.array(lst)
	inc = inc + 1

for line in f:
	instruc = line.replace(' ',',')
	instr_list = instruc.split(',')
	if 'on' in instr_list:
		df.loc[instr_list[-4]:instr_list[-1], instr_list[-5]:instr_list[-2]] = 1
	elif 'off' in instr_list:
		df.loc[instr_list[-4]:instr_list[-1], instr_list[-5]:instr_list[-2]] = -1
	elif 'toggle' in instr_list:
		df.loc[instr_list[-4]:instr_list[-1], instr_list[-5]:instr_list[-2]] = df.loc[instr_list[-4]:instr_list[-1], instr_list[-5]:instr_list[-2]]*-1	
	else:
		sys.exit()

print(df)
print(df.values.sum())
df = df.mask(df < 0, 0)

print(df.values.sum())