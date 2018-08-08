#!/usr/bin/python3
import re
integer = "12345678909"

pattern = re.compile(r'\d{1,3}(?=(\d{3})+(?!\d))', re.DEBUG)
result = pattern.finditer(integer)
for i in result:
  print("Start: ", i.start(), " end: ", i.end())


currency = pattern.sub(r'\g<0>,', integer)
print ("\nCurrency: ", currency)

"""
g<0> indicates all groups identified
g<1> indicates the last group identified
"""

pattern = re.compile(r'\d{1,3}(?=(\d{3})+(?!\d))', re.DEBUG)
list = pattern.findall(integer)
print("\nList:" , list)
