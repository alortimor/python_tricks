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

"""
  The .drop method can be used to remove either columns or rows in-place or
  out of place.
  for example, view the first 5 rows and then remove 2 of them

"""
print(sp500_copy.index[[0,1]]) # this shows the key value for the first 2 rows
print("Before dropping first 2 rows:\n{}".format(sp500_copy[:5]))
sp500_copy.drop(sp500_copy.index[:2],inplace=True)
print("After dropping first 2 rows:\n{}".format(sp500_copy[:5]))

"""
  another way od dropping the first 2 rows is:
    sp500_copy.drop(sp500_copy.head(2).index,inplace=True)

  Out of place removal can be performed using one of these techniques:
  1. sp500_copy=sp500_copy.iloc[2:]
  2. sp500_copy=sp500_copy.tail(-2) # -2 ensures first 2 rows, instead of last 2
  3. sp500_copy.drop(sp500_copy.index[:2],inplace=False)

"""

# All of the previous .drop examples assume axis=0, which is the row.
# iIf columns require removal, then specify axis=1, for example
sp500_copy.drop(['Book Value'],axis=1,inplace=True)
print(sp500_copy)

