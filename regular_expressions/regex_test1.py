#!/usr/bin/python3
import re

pattern = re.compile(r'^<HTML>')

# [:2] means slice of string from the beginning up to the 3rd character,
"""
  for example;
>>> text="Hello World"
>>> text[:3]
'Hel'
>>> text[3:]
'lo World'
>>> text[:-3]
'Hello Wo'
"""
# [2:] means slice of string from the 3rd character up to the end of the string
# since Pythons first character is at position zero
match = pattern.match("  <HTML>"[2:])
if match:
  print("Matched '  <HTML>[2:]' using pattern r'^<HTML>'")
else:
  print("No Match for '  <HTML>[2:]' using pattern r'^<HTML>'")

match = pattern.match("<HTML>")
if match:
  print("Matched '<HTML>' using pattern r'^<HTML>'")

# You can use position to indicate where to start searching from within the string, for example:
pattern = re.compile(r'<HTML>')
if pattern.match("  <HTML>"):
  print("Matched '  <HTML>' using pattern r'<HTML>'")
else:
  print("No Match of '  <HTML>' using pattern r'<HTML>'")

pattern = re.compile(r'<HTML>')
if pattern.match("  <HTML>", 2):
  print("Matched pattern.match('  <HTML>', 2) using pattern r'<HTML>'")
else:
  print("No Match of pattern.match('  <HTML>', 2) using pattern r'<HTML>'")
