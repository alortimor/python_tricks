#!/usr/bin/python3
import pandas as pd
import numpy as np



# Configuring pandas for analysing data in jupyter
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 8)
pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 80)

"""
  Attribute access
  Access an index either:
  1. on a Series
  2. column on a DataFrame
  3. and an item on a Panel directlly as an attribute
"""

# 1.
sa = pd.Series([1,2,3], index=list('abc'))
print(sa.b)
# 2.
dates=pd.date_range('1/1/2019',periods=12)
df=pd.DataFrame(np.random.randn(12,4),index=dates,columns=['A','B','C','D'])
print(df.A)

# 3.
#  using the above dataframe to create a panel
panel=pd.Panel({'actual':df, 'mean':df-df.mean()})
print(panel['mean'])

"""
 Note , .Panel has been deprecated. A message such as the following will appear:
 'Panel is deprecated and will be removed in a future version.
 The recommended way to represent these types of 3-dimensional data are with a MultiIndex
 on a DataFrame, via the Panel.to_frame() method'
"""
