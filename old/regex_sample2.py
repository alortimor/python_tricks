#!/usr/bin/python3

import re
import sys

if __name__ == "__main__":
  """ a, b = 0, 1
  print (a, b)
  n = 10
  while b < n:
    print ("After a, b = b, a+b: a is {} and b is {} is ".format(a, b))
    a, b = b, a+b
"""

  print ("Enter pattern and string to match up, or q/Q to quit")
  # while True:
  p = sys.argv[1]
  s = sys.argv[2]
  # if re.match('[Qq]', p) or re.match('[Qq]', s):
  #   print("\nGoodbye")
  #   break
  if re.match(p, s):
    print("Pattern {} matches string {}".format(p, s))
  else:
    print("Pattern {} does not match string {}".format(p, s))


