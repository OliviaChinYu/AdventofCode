import pandas as pd
import numpy as np


lst = []
for i in range(10):
	lst.append(-1)

df = pd.DataFrame()
inc = 0
for i in range(10):
	# col = str(inc)
	df[inc] = np.array(lst)
	inc = inc + 1

df.loc[2:3, 2:3] = df.loc[2:3, 2:3]*-1

print(df)