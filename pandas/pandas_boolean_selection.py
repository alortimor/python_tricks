#!/usr/bin/python3
import pandas as pd
import numpy as np

s=pd.Series(np.arange(0,5),index=list('abcde'))
logical_results = s >= 3
print(logical_results)
print(s[logical_results])
print("s[s>=2]: {}".format(s[s>=2]))
print("Apply multiple logical expressions s[(s>=2) & s(s<5)]: {}".format(s[(s>=2) & (s<5)]))

print("Use .all(), for example s[s<2].all(), to return true or\n\
false for the logical expression on all rows: {}".format(s[s<2].all() ) )

print("And similarly, for s[s<5].all(), to return true or\n\
false for the logical expression on all rows: {}".format(s[s>5].all() ) )

# you can also apply aggregate functions over rows that satisfy a logical expression
print((s<6).mean())
print((s<6).sum())

