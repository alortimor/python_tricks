#!/usr/bin/python3

if __name__ == "__main__":
  b = bytearray(b"abcdefgh")

  b[4:6] = b"\x15\xa3" # positions [4:6] result in 'ef'
  print(b)

  values = [5, 10, 15, 20]
  arr = bytearray(values)
  
  arr[0:2] = [100, 0, 0] # 5 and 10 are replaced
  for v in arr:
    print(v)

  print('\n')
  # bytearray is mutable, whereas bytes is immutable
  b = bytes([5, 10, 15, 20])
  for v in b:
    print(v)

  # b[0:2] = [100, 0, 0] # this produces an error since it cannot be modified

  # you can use methods such as count, find and in
  b = b"python"
  print("Found at position {}".format(b.find(b"on")))

  print("Number of characters in {} is {}".format(b, b.count(b"p")))
  print("Length of {} is {}".format(b, len(b)))
