#!/usr/bin/python3
import pandas as pd
import numpy as np

pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 8)
pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 80)

sp500=pd.read_csv("sp500.csv",index_col="Symbol",usecols=[0,2,3,7])
print(sp500.head(n=10))

# adding columns out of place
""" all 3 of the techniques for creating new columns, discussed in 
manipulate_df_rename_columns.py
manipulate_df_add_columns.py
namely:
A - sp500_copy['RoundedPrice']=sp500_copy['Price'].round()
B - sp500_copy.insert(2,'DiscountPrice',sp500.Price*0.9)
C - sp500_copy.loc[;, 'NEW_Column']=0
create columns in-place

To create columns as part of a new DataFrame, specify the new column with the value
in a dictionary.
This example creates a DataFrame with a single column
"""

# create a single column DataFrame
rounded_price=pd.DataFrame({'RoundedPrice':sp500.Price.round()})

# you can create a new DataFrame and include all columns by concatenating along 
# the "column" axis=1 (row axis=0 - default)
# e.g.
all_cols_df=pd.concat([sp500, rounded_price],axis=1)
print(all_cols_df) # concatenated DataFrame (across columns)

# one could potentially end up with duplicate column name as a
# result of concatenation across columns

