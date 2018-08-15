#!/usr/bin/python3
"""
Read tuple_sort.py before continuing.
Using 0 and -1 as the index into a list, you can obtain the first and last element respectively. Tulpe unpacking can then be used, if the element in a list is a tuple.
A namedtuple can be used to name each attribute within the tuple.
"""
import operator
from datetime import datetime
from collections import namedtuple

print(__doc__)

phone = namedtuple('phone', ['manufacturer','model_name', 'release_date'])

phones = [('Samsung', 'S7', '11 March 2016'), ('Samsung', 'S8','29 March 2017'), ('Samsung', 'S9', '16 March 2018'),
        ('Google','Pixel', '20 October 2016'),('Google' ,'Pixel 2', '21 October 2017'),
        ('Apple','iPhone 7', '7 September 2016'),('Apple','iPhone 8','1 September 2017'),('Apple','iPhone 9', '12 September 2018')]

def get_key(phone_record):
  return datetime.strptime(phone_record[2], '%d %B %Y')

print("Before sorting\n", phones)
# sorted sorts the phone list, but creates a new list and leaves the original list as is
phones_sorted = sorted(phones, key=get_key)
print("\nAfter sorting\n", phones_sorted)

oldest_model = phone(*phones_sorted[0])
latest_model = phone(*phones_sorted[-1])

print(f"The latest model {latest_model.model_name} was manufactured by {latest_model.manufacturer} and \
was released on the {latest_model.release_date}")

print(f"The oldest model {oldest_model.model_name} was manufactured by {oldest_model.manufacturer} and \
was released on the {oldest_model.release_date}")


print("\nNamed tuples have attributes and methods:\n \
Attributes: _fields, _fields_defaults\n \
Methods: _asdict, _replace, _name")

print("For example latest_model._fields is {} ".format(latest_model._fields))
