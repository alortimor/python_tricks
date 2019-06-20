#!/home/bluefrog/anaconda3/envs/ds_learn/bin/python3
import pandas as pd
import numpy as np

pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 8)
pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 80)

sp500=pd.read_csv("sp500.csv",index_col="Symbol",usecols=[0,2,3,7])
print(sp500.head(n=10))

# adding columns 
# make a copy, before adding new columns, so that the original DataFrame is unchanged
sp500_copy=sp500.copy()


print("Columns of sp500 before adding new column:\n{}".format(sp500_copy.columns))
# now add column to copy
sp500_copy['RoundedPrice']=sp500_copy['Price'].round()
print("DataFrame with new columns, RoundedPrice:\n{}".format(sp500_copy[:2]))
print("\nColumns of sp500 after adding a new column\n{}".format(sp500_copy.columns))


# add a new column using the .loc method
"""
when obtaining a DataFrame slice using .loc['start':'end'], the 'end' is included, unlike
a numpy array, which excludes the ': end'.
for exammple
"""
print(sp500_copy.loc['ABT':]) # this will result in 499 rows, 1 less than is on file.



print("Columns of sp500 before using .loc to add a new column:\n{}".format(sp500_copy.columns))

# specifying an end column that does not exist, along with an initialisation argument,
# will enlarge the dataframe with a new column, for example
sp500_copy.loc[:, 'NEW_COLUMN']=0
print("Columns of sp500 after using .loc to add a new column:\n{}".format(sp500_copy.columns))
