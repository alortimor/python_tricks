#!/usr/bin/python
import re

text = "aba"
pattern = re.compile(r'a?')
list = pattern.findall(text)
print(list)

pattern = re.compile(r'a*')
list = pattern.findall(text)
print(list)

pattern = re.compile(r'a+')
list = pattern.findall(text)
print(list)
