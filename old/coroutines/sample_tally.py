#!/usr/bin/python3

def tally_up():
  total = 0
  while True:
    inc = yield total
    total += inc

if __name__ == "__main__":
  a = tally_up()
  b = tally_up()
  next(a)
  next(b)
  print(a.send(3))
  print(a.send(10))
  print(b.send(2))

