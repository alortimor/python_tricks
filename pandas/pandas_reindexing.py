#!/home/bluefrog/anaconda3/envs/ds_learn/bin/python3
import pandas as pd
import numpy as np

s1=pd.Series(np.arange(10,15),index=['a','b','c','d','e'])
print("pd.Series(np.arange(10,15), index:['a','b','c','d','e'])\n{}".format(s1))

# You can re-index based on a set of keys fewer than the number of values
# in which case the values not indexed will not appear in the series and the
# keys not aligned will equate to NaN, for example
s2 = s1.reindex(['a','c','g'])
print("s1.reindex(['a','c','g'])\n{}".format(s2)) 

# The result of a reindex is a new series. Reindex does not perform in-place modification.
# The new Series has an index with labels, as specified in the passing to the function. 
# The data is copied for each label that exists in the original Series. 

# If a label is not found in the original Series, then NaN will be assigned as the value.
# Finally, rows in the Series with labels that are not in the new index are dropped.

# A common scenario is that one Series has labels of integer type and the other is strings
# but the underlying meaning of the values is the same (this is common when getting data
# from remote sources), for example: 
s1 = pd.Series([0,1,2],index=[0,1,2])
s2 = pd.Series([3,4,5],index=['0','1','2'])
# The result of s1+s2 will be all NaN, since integers cannot align to strings
print(s1+s2)

# Fix by re-indexing (in-place by using index, instead of reindex)
s2.index = s2.index.values.astype(int)
print(s1+s2)

# The .reindex() method has a default behaviour of assigning NaN for values for which keys are unaligned.
# for example:
np.random.seed(123456)
s = pd.Series(np.random.randn(5))
print("pd.Series(np.random.randn(5))\n{}".format(s))
s3 = s.copy()
print("s3 = s.copy()\n{}".format(s3))
s3 = s3.reindex(['a','f'],fill_value=0)
print("s3.reindex(['a','f'],fill_value=0\n{})".format(s3))

s4=pd.Series(['red','green','blue'],index=[0,3,5])
print(s4)

""" ffil is a way of filling in rows into a series, which has gaps in the index.
 The filling occurs based on the previously knwon index, value pair.
 For example:
 0  red
 3  green
 5  blue

 For this series, a gap exists between 0 and 3 and between 3 and 5.
 ffill fills rows between 0 and 3, that is rows 1 and 2, and
 fills rows between 3 and 5, that is rows 4
"""

s4=s4.reindex(np.arange(0,7), method='ffill')
print(s4)

