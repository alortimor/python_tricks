#!/usr/bin/python3
import re
text1 = "Español"
text2 = "Espana"

pattern = re.compile(r"Españ(a|ol)")
match = pattern.search(text1)

print("Without a non-capturing group indicator (?:)")

if match:
  print("groups() ", match.groups() )

pattern = re.compile(r"Españ(?:a|ol)")
match = pattern.search(text1)

print("With a non-capturing group indicator (?:)")
if match:
  print("groups() ", match.groups())
