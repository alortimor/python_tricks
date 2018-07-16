#!/usr/bin/python3

class StringJoiner(list):
  def __enter__(self):
    return self

  def __exit__(self, type, value, tb):
    self.result = "".join(self)

if __name__ == "__main__":
  import random, string
  with StringJoiner() as joiner:
    for i in range(15):
      joiner.append(random.choice(string.ascii_letters))

  print(joiner.result)

