#!/usr/bin/python3

class MyClass:
  i = 12345

  def f(self):
    return "Hello World"

if __name__ == "__main__":
  x = MyClass()
  x.counter = 1
  print(x.counter)

  y = MyClass()
  y.counter = 2
  print(y.counter)
  print(x.counter)
