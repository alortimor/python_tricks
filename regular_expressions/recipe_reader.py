#!/usr/bin/python3

import re

ingredient = "Kumquat: 2 cups"

ingredient_pattern = (r'(?P<ingredient>\w+):\s+(?P<amount>\d+)\s+(?P<unit>\w+)')
pattern = re.compile(ingredient_pattern)
match = pattern.match(ingredient)

print(match.groups())



