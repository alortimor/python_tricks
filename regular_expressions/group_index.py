#!/usr/bin/python3
import re

pattern = re.compile(r'(\w+) (\w+)?')
text = "Hello world"
match = pattern.search(text)

print("match.groups() ", match.groups())
print("match.group(0) ", match.group(0))
print("match.group(1) ", match.group(1))
print("match.group(2) ", match.group(2))
#print("match.group(3) ", match.group(3))

# The following results in the start and end position
# of the string
print(match.start(1))
print(match.end(1))
print(match.start(2))
print(match.end(2))

