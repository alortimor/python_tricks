#!/usr/bin/python3
import pandas as pd
import numpy as np

pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 8)
pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 80)



# SWAPPING COLUMNS

dates=pd.date_range('1/1/2019',periods=12)
df=pd.DataFrame(np.random.randn(12,4),index=dates,columns=['A','B','C','D'])

print("\nUsing .loc[:, '', '' , ..] will not modify DataFrame columns because the column alignment is before value assignment\n")
print("For example, before transform using .loc:\n{}".format(df[['A','B']]))
df.loc[:, ['B','C']] = df[['A','B']]
print("Afer, transform using .loc:\n{}".format(df[['A','B']]))
print("\n-------------------------------")

# you can even re-assign, by swapping the order around, for example
print("Before transform using a simplified (df['B','A']]=df[['A','B']]) approach:\n{}".format(df[['A','B']]))
df[['B', 'A']] = df[['A','B']]
print("After transform:\n{}".format(df[['A','B']]))


# the more efficient and correct way to swap columns values is to convert the
# assigned values to raw data, for example:

df_copy=df.copy()

# assign, after having conversion to raw data
# Note, this line of code only works with pandas version 0.24 and onwards
# Use pd.__version__ to view which version of pandas is imported
df_copy.loc[:, ['B', 'A']]=df_copy[['A','B']].to_numpy()
print(df_copy)



