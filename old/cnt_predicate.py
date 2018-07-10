#!/bin/usr/python3

def is_even(value):
  return (value % 2) == 0
  
def cnt_occurrences(target_list, predicate):
  return sum([1 for e in target_list if predicate(e)])
  
if __name__ == "__main__":
  my_predicate = is_even
  my_list = [2, 4, 6, 7, 9, 11]
  result = cnt_occurrences(my_list, my_predicate)
  print(result)
  
