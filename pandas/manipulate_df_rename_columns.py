#!/home/bluefrog/anaconda3/envs/ds_learn/bin/python3
import pandas as pd
import numpy as np

pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 8)
pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 80)

sp500=pd.read_csv("sp500.csv",index_col="Symbol",usecols=[0,2,3,7])
print(sp500.head(n=10))

# renaming columns 
# renaming a column returns a copy of the DataFrame with the renamed column
sp500_copy=sp500.rename(columns={'Book Value': 'BookValue'})
print(sp500_copy[:2]) # first 2 rows

# instead of making a copy, as a result of a column rename, changing the DataFrame in-place
# is possible with the "inplace=True" attribute setting, e.g.
print("Columns of sp500 before column rename:\n{}".format(sp500.columns))
sp500.rename(columns={'Book Value':'BookValue'},inplace=True)
print("\nColumns of sp500 after column rename:\n{}".format(sp500.columns))

# now possible to use .BookValue property to access data
print(sp500.BookValue[:5])

