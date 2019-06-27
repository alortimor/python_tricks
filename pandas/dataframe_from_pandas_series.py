#!/usr/bin/python3
import pandas as pd
import numpy as np

london_temperatures=pd.Series([19,19])
cape_town_temperatures=pd.Series([13,14])

# create a dataframe from 2 Series's without column names
x=pd.DataFrame([london_temperatures, cape_town_temperatures])
print(x) # lists without column names

# specifying column names for a DataFrame, which is based on a Series,
# will result in values showig up as NaN
# The reason is that the Series has its own index, which must
# align to the DataFrame's in order for the 
x=pd.DataFrame([london_temperatures, cape_town_temperatures],columns=['London','Cape Town'])
print(x)

# for setup of a DataFrame using a Series as a source,
# specify column names using the .columns property, since
# due to alignment of keys values will be NaN otherwise
x=pd.DataFrame([london_temperatures, cape_town_temperatures])
x.columns=['London','Cape Town']
print(x)

# multiple series's can also be setup (with column names) as a DataFrame,
# by specifying them in a dictionary, for example


london_temperatures=pd.Series([19,19])
cape_town_temperatures=pd.Series([13,14])
df=pd.DataFrame({'London': london_temperatures, 'Cape Town': cape_town_temperatures})
print(df)

