#!/usr/bin/python3
import re

"""
 Yes-No pattern notation:
 (?(id/name)yes-pattern|no-pattern)

Translates to :
If the group with the specific "id" or "name" has already been
matched, then the yes pattern has to match.
If the group has not been matched then the no-print(pattern
has to match.
"""

# for example:
code1="34-erte-22"
code2="erte"
print(r"Regular expression: '(\d\d-)?(\w{3,4})(?(1)(-\d\d))'")
pattern = re.compile( r'(\d\d-)?(\w{3,4})(?(1)(-\d\d))' )

match = pattern.match(code1)
if match:
  print(code1, " matches")
else:
  print(code1, " does not match")

match = pattern.match(code2)
if match:
  print(code2, " matches")
else:
  print(code2, " does not match")

#pattern = re.compile(

# (?: (?:One() |\1Two()| \1\2Three() | John Malkovich | Stamos | Travolta ) \|? )* $             
