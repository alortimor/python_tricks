#!/usr/bin/python3
"""
Sample text:
My favourite gospel is John, The other John (John the Baptist) is based on the prophecy of the 2nd coming of Elijah.
The gospel of John is equally a rich exposition of the righteousness and grace of God.

Assuming the following RE: r'John(?!\sthe\sBapist)'

In the above text, 'John the Baptist' is matched for the RE and therefore should be excluded from the grouping.
This is the premise for a negative look ahead.
The negative look ahead is (?!regex), as opposed to the positive look ahead, which is (?=regex)
"""
import re
print(__doc__)

text1 ="My favourite gospel is John, \
The other John (John the Baptist) is based on the prophecy of the 2nd coming of Elijah. \
The gospel of John is equally a rich exposition of the righteousness and grace of God."

pattern = re.compile(r'John(?!\sthe\sBaptist)')

result = pattern.finditer(text1)
for i in result:
    print("Start: ", i.start(), " End: ", i.end())

list = pattern.findall(text1)
print("List: ", list)

"""
for r'John(?!\sthe\sBaptist)'), 3 John's will be identified, whereas for
r'John(?=\sthe\sBaptist)' only a single John will be identified, since the latter is a
positive look ahead based on 'John the Baptist', and the former is negative look ahead.
"""
text2 = "There are several individuals that I can name, John McDonald, John Kettering and John the Baptist"
pattern = re.compile(r'John(?!\sthe\sBaptist)')

print ("\n" + text2 + "\n")
result = pattern.finditer(text2)
for i in result:
  print("Start: ", i.start(), " End ", i.end())

