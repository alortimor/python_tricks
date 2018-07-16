#!/usr/bin/python3

from functools import total_ordering

@total_ordering
class WeirdSort:
  def __init__(self, string, number, sort_num):
    self.string = string
    self.number = number
    self.sort_num = sort_num

  def __lt__(self, object):
    if self.sort_num:
      return self.number < object.number
    return self.string < object.string

  def __repr__(self):
    return "{}:{}".format(self.string, self.number)

  def __eq__(self, object):
    return all((self.string == object.string,
                self.number == object.number,
                self.sort_num == object.number))

if __name__ == "__main__":
  a = WeirdSort('a', 4, True)
  b = WeirdSort('b', 3, True)
  c = WeirdSort('c', 2, True)
  d = WeirdSort('d', 1, True)

  l = [a,b,c,d]
  print(l)
  l.sort()
  print(l)

  for i in l:
    i.sort_num = False

  l.sort()
  print(l)
