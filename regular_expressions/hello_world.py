import re
print("Hello World")

pattern = re.compile(r'^<HTML>')
match = pattern.match("<HTML>")
if match:
  print("Matched '<HTML>' using pattern r'^<HTML>'")


