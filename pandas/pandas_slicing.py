#!/home/bluefrog/anaconda3/envs/ds_learn/bin/python3
import pandas as pd
import numpy as np

s1=pd.Series(np.arange(10,15),index=list('abcde'))
print(s1)
print(s1['a'])
# you can provide a list of keys
print(s1[['a','d']])
# or you can provide a list of index numbers
print(s1[[3,1]])


# you can perform a key lookup using .iloc
print(s1.loc['a'])
# or a position lookup
print(s1.iloc[0])

s=pd.Series(np.arange(100,110),index=np.arange(10,20))

print(s)
print("s[1:6]\nP{}".format(s[1:6]))
print("s.iloc[[1,2,3,4,5]] equivalent to s[1:6]:\n{}".format(s[1:6]))

print("First four, but only every 2nd item, s[:4:2]:\n{}".format(s[:4:2]))
print("First four, s[:4]:\n{}".format(s[:4]))
print("4th position to the end, but only every 2nd item s[4::2]:\n{}".format(s[4::2]))
print("Last 2 rows s[-2:]:\n{}".format(s[-2:]))

print("All rows apart from last 4 s[:-4]:\n{}".format(s[:-4]))
print("Last 4 s[:-4]:\n{}".format(s[-4:]))
print("The first three of the last four s[-4:-1]:\n{}".format(s[-4:-1]))
print("s.tail(4).head(3) is equivalent to s[-4:-1]:\n{}".format(s.tail(4).head(3)))