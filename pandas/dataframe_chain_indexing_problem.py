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
  of (slice(None),('one','second')) to a single call of __getitem__.
  This allows pandas to deal with this as a single entity. 
  Additionally, the order of operations can be significantly faster, and allows one to index both
  axes if desired.
"""

# Assigning to a chained index can lead to unpredictable results, for example

df_product_idx['one']['second']='x' # method 1 assignment
# becomes
# df_product_idx.__getitem__('one').__setitem__('second', 'x')

# whereas
df_product_idx.loc[:, ('one','second')]='x' # method 2 assignment
# becomes
# df_product_idx.loc.__setitem__((slice(None), ('one','second')),'x')

"""
  Notice that method 1 has an additional __getitem__ !
  It is hard to predict whether the __getitem__ will return a view or a copy.
  It all depends on the memory layout of the array at the point of the assignment, 
  which pandas makes no gurantees about.
  Therefore, whether the __setitem__ will modify df_product_idx or a temporary object,
  that will be immediately discarded, is unknown.

  The "SettingWithCopyWarning" warning was created to flag such potentially confusing
  "chained" assignments, since such assignments often result in unpredicatble behaviour.
  This is especially the case when the first selection returns a copy, which may or may not occur.
  Hence, the "SettingWithCopyWarning" warning appears when attempting method 1 types of assignments.
  Note therefore, such assigments should be avoided due to unpredictable behaviour.

  Additionally, "SettingWithCopyWarning" is associated with further text, namely:
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer]=value instead
  to assist with implementing the recommended method 2 type assignment.

  use this setting to ensure warning appear:
  pd.set_option('mode.chained_assignment','warn')
"""


# Evaluation order often determines whether a copy or the original DataFrame is being modified.
dfb=pd.DataFrame({'a':['one','one','two','three','two','one','six'],'c': np.arange(7)})
print(dfb)

# The following updates the original, not the copy, even though the "SettingWithCopyWarning" occurs
dfb['c'][dfb.a.str.startswith('o')]=42

# The following however updates the copy, not the original
dfb[dfb.a.str.startswith('o')]['c']=42

# Regardless, use .loc, since, as is apparent from previous discussion and examples, the outcome
# is unpredicatble
# for exampe (correct way):
dfb.loc[dfb.a.str.startswith('o'), 'c']=33
print("DataFrame updated with recommended method:\n{}".format(dfb))



