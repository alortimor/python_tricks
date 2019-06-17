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


# one can use .concat() to combine dataframes or series's.
# When concating a series to a dataframe, the resulting type is a dataframe
d = pd.DataFrame([1], index=['a'])
s=pd.Series([2], index=['b'])
x=pd.concat([d,s])
print(type(x))
# one can ignore existing indexes for the dataframe and/or series being combined,as follows:
x=pd.concat([d,s], ignore_index=True)
# one can create a new index when contating, for example
y=pd.concat([d,s], keys=['c','d'])
print(y)


