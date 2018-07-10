#!/usr/bin/python3

import pickle

if __name__ == "__main__":
  some_data = ["A", "B", ["C", "D"], ("E", "F")]

  with open("pickled_list", "wb") as file:
    pickle.dump(some_data, file)  

  with open("pickled_list", "rb") as file:
    loaded_data = pickle.load(file)  

  print(loaded_data)
  assert loaded_data == some_data
