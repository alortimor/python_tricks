#!/usr/bin/python3
import re

pattern = re.compile(r"^\w+: (\w+/\w+/\w+)")

list = pattern.findall("date: 12/01/2013 \ndate: 11/01/2018")

print(list)

# if you include a multiline , then the search continues across new lines (\n)
pattern = re.compile(r"^\w+: (\w+/\w+/\w+)", re.M)

list = pattern.findall("date: 12/01/2013 \ndate: 11/01/2018")
print(list)

