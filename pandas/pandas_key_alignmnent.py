#!/usr/bin/python3
import pandas as pd
import numpy as np

s=pd.Series(np.arange(0,5),index=list('abcde'))

print("Sample series:\n{}".format(s))
print("Slice s[1:3]:\n{}".format(s[1:3])) # 2nd to 3rd

print("Slice s[1:3] is equivalent to s['b':'c']:\n{}".format(s['b':'c']))

s1=pd.Series([1,2],index=['a','b'])
s2=pd.Series([4,3],index=['b','a'])
s3=pd.Series([5,6],index=['b','c'])
print("pd.Series([1,2],index=['a','b'])\n{}".format(s1))
print("pd.Series([4,3],index=['b','a'])\n{}".format(s2))
print("pd.Series([5,6],index=['b','c'])\n{}".format(s3))
print("s1+s2:\n{}".format(s1+s2))
print("s2-s1:\n{}".format(s2-s1))
print("Note, 'a' and 'c' do not align, for s1+s3, hence they set to NaN\n{}".format(s1+s3))

s1=pd.Series([1.0,2.0,3.0],index=['a','a','b'])
s2=pd.Series([4.0,5.0,6.0,7.0],index=['a','a','c','a'])
print("pd.Series([1.0,2.0,3.0],index=['a','a', 'b'])\n{}".format(s1))
print("pd.Series([4.0,5.0,6.0,7.0],index=['a','a','c','a'])\n{}".format(s2))
print("Note, 'b' and 'c' do not align, hence they set to NaN, for s1+s2\n{}".format(s1+s2))

