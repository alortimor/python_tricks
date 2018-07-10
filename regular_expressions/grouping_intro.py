#!/usr/bin/python3
import re
text1 = "Espanol"
text2 = "Espana"

pattern = re.compile("Espan[aol]")
match = pattern.search(text1)

if match:
  print(text1, " matched")

# the problem is the following, "Espanl" would also match
text1 = "Espanl"

pattern = re.compile("Espan[aol]")
match = pattern.search(text1)

if match:
  print(text1, " matched")
else:
  print(text1, " not matched")

# so in order to avoid the second match an "or" is used in
# the character class, and the character class is grouped using ()

pattern = re.compile("Espan(a|ol)")

text1 = "Espanol"
match = pattern.search(text1)

if match:
  print(text1, " matched")

text1 = "Espanl"
match = pattern.search(text1)

if match:
  print(text1, " matched")
else:
  print(text1, " not matched")
