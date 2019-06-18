#!/home/bluefrog/anaconda3/envs/ds_learn/bin/python3
import pandas as pd
import numpy as np


london_temperatures=[19,19,23,25]
cape_town_temperatures=[16,15,13,14]


temperatures={'London': london_temperatures,
              'Cape Town': cape_town_temperatures}

x=pd.DataFrame(temperatures)
print(x)

print(x['London'])
print(x[['London','Cape Town']])

