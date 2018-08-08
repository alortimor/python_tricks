#!/usr/bin/python
"""
A MatchObject represents the matched pattern, based on a RE specification.
A MatchObject is returned if a match is made against a matched object.

A function, that takes MatchObject as a parameter, can be used to process groups matched by () within the RE.
Difference between 'match' and 'search' is that 'search' tries to match the RE at any location of the string, no only at the beginning, which is what the match does.
"""
import re
print(__doc__)

def normalize_orders(matchobj):
  if matchobj.group(1) == '-':
    return 'A'
  else:
    return 'B'

pattern = re.compile('([-|A-Z])')
list = ["-1234", "A193", "C124"]
for code in list:
  print(pattern.sub(normalize_orders, code))

