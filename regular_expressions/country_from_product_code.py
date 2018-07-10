#!/usr/bin/python3
import re

pattern = re.compile(r'(\d+)-(\w+)')
products = r"1-a\n20-baer\n34-afcr"

match = pattern.finditer(products)
for country in match:
  print ("Country : " , country.group(1), " Code: ", country.group(2))

