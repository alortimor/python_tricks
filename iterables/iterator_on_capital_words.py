#!/usr/bin/python3

class CapitalIterable:
  def __init__(self, string):
    self.string = string

  def __iter__(self):
    return CapitalIterator(self.string)

class CapitalIterator:
  def __init__(self, string):
    self.words = [w.capitalize() for w in string.split()]
    self.index = 0

  def __next__(self):
    if self.index == len(self.words):
      raise StopIteration()

    word = self.words[self.index]
    self.index += 1
    return word

  def __iter__(self):
    return self

if __name__ == "__main__":
  iterable = CapitalIterable("the quick brown fox jumps over the lazy dog")
  iterator = iter(iterable)
  while True:
    try:
      print(next(iterator))
    except StopIteration:
      break

  print('\n')
  for i in iterable:
    print(i)

  print('\n')
  print([i for i in iterable])
