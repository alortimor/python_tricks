#!/usr/bin/python3

import re

ingredient = "Kumquat: 2 cups"

ingredient_pattern = (r'(?P<ingredient>\w+):\s+(?P<amount>\d+)\s+(?P<unit>\w+)')

# The above can also be coded as follows for better readibility:
pattern = re.compile(
    r'(?P<ingredient>\w+):\s+'
    r'(?P<amount>\d+)\s+'
    r'(?P<unit>\w+)'
)

match = pattern.match(ingredient)

print(match.groups())
print(match.group('ingredient'))
print(match.group('amount'))
print(match.group('unit'))

