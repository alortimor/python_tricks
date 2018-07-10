#!/usr/bin/python3

class Wrapped():
  pass

def shout(Wrapped):
  def inner(*args, **kwargs):
    print("BEFORE")
    w = Wrapped
    ret = Wrapped(*args, **kwargs)
    print("AFTER")
    return ret
  return inner

@shout
def doge():
  print('such wow!')

def count(wrapped):
  def inner(*wargs, **kwargs):
    inner.counter += 1
    return wrapped 

if __name__ == "__main__":
  doge()
