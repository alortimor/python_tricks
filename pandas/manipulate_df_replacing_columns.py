#!/usr/bin/python3
import pandas as pd
import numpy as np

pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 8)
pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 80)

sp500=pd.read_csv("sp500.csv",index_col="Symbol",usecols=[0,2,3,7])

# The contents of a DataFrame column can be replaced by assigning a new series to the existing
# column.
# One can do this using the [] operator.
# for example:

# replacing the column contents with a pandas Series occurs in-place
# hence make a copy beforehand, so that the original is unchanged.
sp500_copy = sp500.copy()


# create a series based on the rounded figure of thr Price column
rounded_price=pd.DataFrame({'Price':sp500.Price.round()})
print("type(rounded_price)): {}".format(type(rounded_price)))

# replace the Price columns with a rounded figire of the original Price
sp500_copy.Price = rounded_price.Price
print(sp500_copy)

# column contents can also be replacxed in-place using the .loc method
# with a slice.
# First, set back to the original
sp500_copy = sp500.copy()
# replace columns using a .loc slice
sp500_copy.loc[:, 'Price']=rounded_price.Price
print(sp500_copy[:5]) # show the first five rows to confirm contents was replaced

