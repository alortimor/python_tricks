#!/usr/bin/python3
import pandas as pd
import numpy as np


london_temperatures=[19,19]
cape_town_temperatures=[13,14]


x=pd.DataFrame([london_temperatures, cape_town_temperatures])
print(x) # lists without column names


x=pd.DataFrame([london_temperatures, cape_town_temperatures],columns=['London','Cape Town'])
print(x)

# Notice the number of columns must match the number of elements in the list, otherwise
# an error will be generated

# columns can be renamed implicitly with the.columns property, for example
df = pd.DataFrame({'x':[1,2], 'y':[10,20]})
print(df)
print(df.columns) # columns names will be x,y

# column={'old name':'new name', '..':'.. .. }
df=df.rename(columns={'x':'a', 'y':'b'})

# columns names will now be shown as a,b
print(df)


