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

print("Using pattern.findall(string, [pos[, endpos]]) for the string 'hello world'")
pattern = re.compile(r'\w+')

print("Will produce the following when printed")
print(pattern.findall("hello world"))

print("and when iterated over, will show as follows")
for w in pattern.findall("hello world"):
  print(w)

pattern = re.compile(r'a*')
print ("How to use findall(string[, pos[, endpos]]) using pattern = re.compile(r'a*') with string 'aba'")
pattern.findall("aba")

print("Will produce the following when printed")
print(pattern.findall("aba"))

"""
Because of the '*' quantifier, which allows 0 or more repetitions of the preceding regex;
The regex matches the first character 'a', then it follows with 'b'.
There is a match due to the '*' quantifier, since '*' can match 0.
"""

print("and when iterated over, will show as follows")
for w in pattern.findall("aba"):
  print(w)


print ("using pattern = re.finditer(r'(\w+) (\w+)') on 'hello world hola mundo'")
pattern = re.compile(r"(\w+) (\w+)")
print(pattern.findall("hello world hola mundo"))


for w in pattern.findall("hello world hola mundo"):
  print(w)
  for x in w:
    print(x)
  
