#!/home/bluefrog/anaconda3/envs/ds_learn/bin/python3
import pandas as pd
import numpy as np

pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 8)
pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 80)

sp500=pd.read_csv("sp500.csv",index_col="Symbol",usecols=[0,2,3,7])
print(sp500.head(n=10))

# adding columns out of place
# all 3 of the techniques for creating new columns, discussed in 
