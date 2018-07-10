#!/usr/bin/python3
import re
pattern = re.compile(r"(?u)\w+")
list = pattern.findall(r"ñ")
print(list)
