#!/usr/bin/python3
import pandas as pd
import numpy as np

pd.set_option('display.max_column',10)
pd.set_option('display.max_rows',15)
pd.set_option('display.width',120)

dates=pd.date_range('1/1/2019',periods=12)
print(type(dates))

# Use dates as the index for setting up a DataFrame
print("Dates DataFrame (pd.date_range('1/1/2019',periods=12) :n{}".format(dates))


df=pd.DataFrame(np.random.randn(12,4),index=dates,columns=['A','B','C','D'])
print("pd.DataFrame(np.random.randn(12,4),index=dates,columns=['A','B','C','D']):\n{}".format(df))

# A pandas panel is a 3D container of data. 
"""
The 3 axes are :
items − axis 0, each item corresponds to a DataFrame contained inside.
major_axis − axis 1, it is the index (rows) of each of the DataFrames.
minor_axis − axis 2, it is the columns of each of the DataFrames.

So basically, a panel constitutes rows of dataframes.
Constructor for panels: pndas.Panel(data, items, major_axis, minor_axis, dtype, copy)
"""

# example of a panel:

data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)

# using the above dataframe to create a panel
panel=pd.Panel({'actual':df, 'mean':df-df.mean()})
print(panel)
print(panel['mean'])

# [] is a way to use the index, for example
s=df['A'] # s is of type pandas Series, since only a single column was assigned
print(s)

# obtain the index value for row five in the dates (assigned on line 5)
# dataframe, which is of type DatetimeIndex
print("\ndates[5]: {}".format(dates[5]))

# use the index value from row 5, as an index for s
print("\ns[dates[5]]: {}".format(s[dates[5]]))

