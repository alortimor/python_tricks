#!/usr/bin/python3
import pandas as pd
import numpy as np
sp500=pd.read_csv("sp500.csv",index_col="Symbol",usecols=[0,2,3,7])
print(sp500.head)
# view the number of rows
print(len(sp500))
# view the dimensions
print(sp500.shape) # should be 500 x 3
print(sp500.size) # size returns row count x column count, i.e. 500*3
print(sp500.index) # index of the data frame consists of the symbols for the 500 stocks
print(sp500.columns) # columns consist of columns, without Symbol (since this is the key)

# to select a single columns, simply specify column name as a subscript to the DataFrame
print(sp500['Sector'].head())
# When a single column is retrieved from a DataFrame, the result is a Series
print(type(sp500['Sector']))
# To specify more than a single column, specify a list, same as for a series
# When more than one column is retrieved, the result is a DataFrame
print(type(sp500[['Sector','Price']]))

# One can also retrieve a column by specifying column name as an attribute
# for example:
print(sp500.Price)

# Use .loc and .iloc to retrieve a row based on either key value or row position
# for example
print (sp500.loc['MMM']) # single column
print(sp500.loc[['MMM','MSFT']]) # multiple columns

# or by row position
print (sp500.iloc[0]) # single column
print (sp500.iloc[[0,2]]) # multiple column


# It ispossible to identify row position, by using .get_loc method
# of the index property, with the key,
# and then using the returned row position to retrieve the row, for example
r1=sp500.index.get_loc('MMM')
r2=sp500.index.get_loc('A')

print(r1, r2) # should be 0 and 10
# One can then use .iloc passing r1 and r2, e.g.
print(sp500.iloc[[r1,r2]])

# Use .at[] and .iat[] to perform scalar lookups (individal values)
print(sp500.at['MMM','Price'])
print(sp500.iat[0,1])

