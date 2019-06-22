#!/usr/bin/python3
import pandas as pd
import numpy as np

pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 8)
pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 80)

sp500=pd.read_csv("sp500.csv",index_col="Symbol",usecols=[0,2,3,7])

# columns can be dropped using 1 of 3 methods:
# 1. del method - in-place deletion
# 2. pop()      - in-place deletion
# 3. drop(labels,axis1) - out of place deletiion. returns a new dataframe

# make a copy first, so that the orignal remains unchanged
sp500_copy=sp500.copy()

print("Before column deletion:\n{}".format(sp500_copy[:2]))
# delete a the Book Value column
del sp500_copy['Book Value']
print("After column deletion:\n{}".format(sp500_copy[:2]))

# pop() can be be used to remove a column, but retain the column
# contents in a new DataFrame, for example

sp500_copy=sp500.copy() # set back to the original
print("Before column popping:\n{}".format(sp500_copy[:2]))
popped=sp500_copy.pop('Sector')
print("After column popping:\n{}".format(sp500_copy[:2]))

