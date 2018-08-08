#!/usr/bin/python
"""
When performing alternation, for example for against the following text:
English|Englishmen
E - E
n - n
g - g
l - l
i - i
s - s
h - h
  - m

At the point where a match is unsuccessfull ('m' in this case), the RE backtracks
and starts again at 'E' for the next option (Englishmen).
This is referred to as catastrophic backtracking. A known issue with regular expressions.
Worst case scenario with catastrophic backtracking is that a stack overflow can occur, and
best case scenario is a very inefficient slow performing regular expression.
"""
import re
from time import clock as now

print(__doc__)

def test(f, *args, **kwargs):
  start = now()
  f(*args, **kwargs)
  print("The function {} lasted {} ".format(f.__name__, now()-start))

def catastrophic(n):
  print("Testing with {} characters".format(n))
  pat = re.compile(r'(a+)+c')

  text = "%s" %('a' * n)
  match = pat.search(text)

for n in range(20,30):
  test(catastrophic,n)
