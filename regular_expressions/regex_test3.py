#!/usr/bin/python3
import re
# print("Hello World")

"""
* = 0 or more
+ = 1 or more
? = 0 or 1
{2} = exactly 2
{2,5} = between 2 and 5
{2,} = 2 or more
{,5} = up to 5
"""


print ("using pattern = re.finditer(r'(\w+) (\w+)') on 'hello world hola mundo'")
pattern = re.compile(r"(\w+) (\w+)")
print(pattern.findall("hello world hola mundo"))

for w in pattern.findall("hello world hola mundo"):
  print(w)
  for x in w:
    print(x)

print("Now investigate pattern.finditer('Hello world hola mundo')")  
"""
Its working is essentially the same as findall , but it returns an iterator in which
each element is a MatchObject
"""
pattern = re.compile(r'(\w+) (\w+)')
hit = pattern.finditer("hello world hola mundo")
print("Now perform a __next__()")
match = hit.__next__() ## determine if a match in fact occurs before
                       # referencing group or groups
if match:
  print("match.groups() ", match.groups())
  print("match.group(0) ", match.group(0))
  print("match.group(1) ", match.group(1))
  print("match.group(2) ", match.group(2))

  ## This generates an error: print("match.group(2) ", match.group(2))

print("Now perform a __next__() again")
match = hit.__next__()
print("match.groups() ", match.groups())
print("match.group(0) ", match.group(0))
print("match.group(1) ", match.group(1))
print("match.group(2) ", match.group(2))

# Also, you can use match.span()
print("value for match.span(): ", match.span())

for hit in pattern.finditer("hello world hola mundo"):
  print(hit.group())

# for match in pattern.finditer("hello world hola mundo"):
#  print(match)
