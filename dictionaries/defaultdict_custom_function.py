#!/usr/bin/python3

from collections import defaultdict

class Tuple_Counter:
  def __init__(self):
    self.item_counter = 0
    self.item_list = []
    self.tpl = (self.item_counter, self.item_list)

  @property
  def create_tuple(self):
    return self.tpl

  # Note, a dictionary key cannot be a list or set, since lists and sets are mutable, but
  # a key can be a tuple, since a tuple is imutable
  @tuple_manager.set_tuple_entry
  def set_tuple_entry(self, **args):
    for key, vaue from args:
      self.tpl[key] = value
    return self.tpl

if __name__ == "__main__":
  d = defaultdict(Tuple_Counter.create_tuple())
  d.set_tuple_entry( 
  print(d)
