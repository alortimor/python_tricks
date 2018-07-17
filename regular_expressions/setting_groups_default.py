#!/usr/bin/python3
import re

text="Hello World"
# the ? prevents any further matching, other than a first and second word separated
# by a space
pattern = re.compile(r'(\w+) (\w+)?')

"""
When using groups, you can specify a default value, which is the value
shown when a match is not found.
The value shown is "None" if no default is supplied
"""

match = pattern.search("Hello ")
# with a default value
print(match.groups("World"))

# without a default value
print(match.groups())

