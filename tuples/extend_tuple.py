#!/usr/bin/python3

class MyTuple(tuple):
  def __new__ (*args):
    tpl = tuple().__new__(*args)
    tpl.my_list = []
    return tpl

  def __getitem__(self, key):
    return super(MyTuple, self).__getitem__(key-1)

if __name__ == "__main__":
  tpl = MyTuple(("A", "B"))
  tpl.mylist = ["C", "D"]
  for char in tpl:
    print(char)

  for char in tpl.mylist:
    print(char)
