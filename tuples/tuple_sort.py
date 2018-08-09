#!/usr/bin/python3
"""
Tuples are immutable. They can be considered as 'immutable lists'.
However, another way of understanding them is to think of them as read-only
database records. The number of columns and rows become relevant depending
on the type of processing required.
The order can be sorted by 
"""

import operator
from datetime import datetime

phones = [('Samsung S7', '11 March 2016'), ('Samsung S8','29 March 2017'), ('Samsung S9', '16 March 2018'),
        ('Google Pixel', '20 October 2016'),('Google Pixel 2', '21 October 2017'),
        ('Apple iPhone 7', '7 September 2016'),('Apple iPhone 8','1 September 2017'),('Apple iPhone 9', '12 September 2018')]

def get_key(phone_record):
  return datetime.strptime(phone_record[1], '%d %B %Y')

print("Before sorting\n", phones)
# sorted sorts the phone list, but creates a new list and leaves the original list as is
phones_sorted = sorted(phones, key=get_key)
print("\nAfter sorting\n", phones_sorted)

phones.sort(key=get_key)
print("\nOriginal list sorted\n",phones) 


