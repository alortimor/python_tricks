#!/usr/bin/python3

from collections import defaultdict
num_items = 0
def tuple_counter():
  global num_items
  num_items += 1
  return (num_items, [])

if __name__ == "__main__":
  d = defaultdict(tuple_counter)
  d['a'][1].append("hello")
  d['b'][1].append("world")
  d['a'][1].append("goodbye")
  print(d)
