#!/home/bluefrog/anaconda3/envs/ds_learn/bin/python3
import pandas as pd
import numpy as np

s1=pd.Series(np.arange(10,15),index=['a','b','c','d','e'])


print(s1)

# one can add new rows, through assignment of the key value subscript to the value, e.g
s1['f']=100
print("Additional item added s1['f']=100\n{}".format(s1))

s1['f']=101
print("Data items can modified in-place s1['f']=101\n{}".format(s1))

del(s1['f'])

print("Data items can remove del(s1['f']) \n{}".format(s1))

