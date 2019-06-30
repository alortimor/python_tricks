#!/usr/bin/python3
"""
Slicing a dataframe with [] is much the same as slicing a series, as described in pandas_slicing.py.
One can use labels to slice, for example
"""
import pandas as pd
import numpy as np


print(__doc__)

df=pd.DataFrame(np.random.randn(12,4), columns=list('ABCD'),index=pd.date_range('20190101',periods=12))

print(df)

"""
  .loc is strict when you present slicers that are not compatible (or convertible) with the index type.
  For example using integers in DatetimeIndex will raise a TypeError
"""
# print(df.loc[2:3]) # this generates a TypeError

# one can use labels to slice a dataframe, e.g.
print(df.loc['20190101':'20190104']) # default is american format yyyyddmm


# you can slice in steps
print(df['20190101': : 2]) # every second row

# you can slice with .loc, but only output selected columns, for example
print(df.loc['20190101':, ['A','C']]) # only outputs columns A and C


# you can slice columns as well, instead of selecting specific columns as per the previous example,
# for example
print(df.loc['20190101':, 'A':'C']) # outputs column A through to column C

# output a selected number of rows, based on a list of the index literal values, for example
print(df.loc[ ['20190101'], :])


