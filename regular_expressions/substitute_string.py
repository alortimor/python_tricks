#!/usr/bin/python3
import re

pattern = re.compile(r'[0-9]+')
order_list = "order0 order1 order13"
print("Before substitution " , order_list)
order_list = pattern.sub('-', order_list)
print("After substitution using re.sub(r'[0-9]+'): " , order_list)

# Note, regardless of the number of digits, all digits were replaced by a single "-"

# It replaces the leftmost non-overlapping occurrences of the pattern, for example
pattern = re.compile('00')
order_str = 'order00000'
print("Before substitution " , order_str)
order_str = pattern.sub('-', order_str)
print("After substitution using re('00'): " , order_str)

# You can use a function in place of the substitution character
def normalize_orders(matchobj):
  if matchobj.group(1) == '-':
    return 'A'
  else:
    return 'B'

order_list2 = '-1234, A193  B123'
pattern = re.compile(r'([-|A-Z])')
order_list2 = pattern.sub(normalize_orders, order_list2)
print(order_list2)






