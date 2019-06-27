#!/usr/bin/python3
import pandas as pd
import numpy as np

# import datetime
# from datetime import datetime, date

# use numpy array as a source for a DataFrame
x=pd.DataFrame(np.array([[10,11],[20,21]])) # setup a 2x2 dataframe 
print(x)

x=pd.DataFrame(np.array([[10,11],[20,21]])) # setup a 2x2 dataframe 


# if columns names are not specified, pandas creates a RangeIndex to name columns.
print(x.columns)

x=pd.DataFrame(np.array([[10,11],[20,21]]),columns=['abc','xyz']) # setup a 2x2 dataframe,with column names

# x.columns will now show be shown as index, with column names in a list
print(x.columns)

print("\nlen(x) returns number of rows: {}".format(len(x)))
print("\nx.shape returns dimensions: {}".format(x.shape))
