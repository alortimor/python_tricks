#!/usr/bin/python3
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

s=pd.Series(['x','y','z'],index=[0,1,2])
print(s)

# when using slicing, the result of the slice is a view into the original Series.
# Modification of values through the result of the slice operation will modify the original Series.
# for example

a_slice=s[:2]
print(a_slice)

# The following assignment of a value to an element of a slice will change the value in the original Series
a_slice[0] ='a'
# hence when viewing the original, s, one can see the changed value
print(s)
"""
  print(s) will result in 0 'a', 1 'y' , 2 'z'
"""
