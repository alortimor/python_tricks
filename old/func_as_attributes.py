#!/usr/bin/python3


class A:
  def print(self):
    print("my class is A")

def fake_print():
  print("my class is not A")

if __name__ == "__main__":
  a = A()
  a.print()
  a.print = fake_print
  a.print()

  
