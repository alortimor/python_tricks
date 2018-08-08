#!/usr/bin/python3
import re
import cProfile
from time import clock as now

def test(f, *args, **kwargs):
  start = now()
  f(*args, **kwargs)
  print("The function {} lasted {} ".format(f.__name__, now()-start))

def alternation(text):
  pattern = re.compile(r'spa(in|iard)')
  pattern.search(text)

test(alternation, "spain")
cProfile.run("alternation('spaniard')")
