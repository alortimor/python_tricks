#!/usr/bin/python3
import pandas as pd
import numpy as np

"""
When setting values in a pandas object, avoid what is called chained indexing!

"""


# Refer to this online documentation for a better understanding of MultiIndex:
# http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.MultiIndex.from_product.html

# for example
df_product_idx=pd.DataFrame( [list('abcd'),list('efgh'),list('ijkl'),list('mnop')]
                           ,columns=pd.MultiIndex.from_product([['one','two'],['first','second']]))
print(df_product_idx)

# the 2nd columns can be accessed in one of two ways:
# 1.
print(df_product_idx['one']['second'])
# 2.
print(df_product_idx.loc[:, ('one','second')] )

print(df_product_idx['one'])

"""
  The above 2 column access methods both yield the same results.
  However, given the order of operation on these, method 2 (using .loc) is preferred, (and more efficient)
  over methd 1 (chained [][]).
  df_product_idx['one'] selects the first level of columns and returns a DataFrame that is singly-indexed.
  Then another Python operation, df_product_idx_with_one['second'] selects the series indexed by 'second'. 
  This is indicated by the variable df_product_idx_with_one because pandas views these operations as separate
  events, for example separate calls to __getitem__, so it has to treat them as lineat operations, that happen
  one after the other.

  df_product_idx.loc[:,('one','second')] on the other hand passes a nested tuple 
  of (slice(None),('one','second')) to a single call to __getitem__.
  This allows pandas to deal with this as a single entity. 
  Additionally, the order of operations can be significantly faster, and allows one to index both
  axes if desired.
"""
