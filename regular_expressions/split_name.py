#!/usr/bin/python3
import re
# full_name = input("Full name: ")
full_name = "Peter Todd"
print("Hello ", full_name)
#pattern = re.compile(r"^(?P<first_name>\w{1}) (?P<middle_names>\w*) (?P<last_name>\w{1})$")
pattern = re.compile(r'(\w+) (\w+)')
result = pattern.match(full_name)
print("result.group(0) ", result.group(0)) # This result in "Peter Todd"
print("result.group(1) ", result.group(1)) # This results in ""
print("result.group(2) ", result.group(2)) # This results in "Todd"


# If I use te following regular expression instead:
pattern = re.compile(r'(\w)+')
result = pattern.match(full_name)
print("result.group(0) ", result.group(0)) # This result in "Peter"
print("result.group(1) ", result.group(1)) # This results in "r"


# What I'm actually after is a tuple of
# ('Peter', 'Todd')

pattern = re.compile(r'^(\w+) (\w+)$')
names = pattern.finditer("Hello World")
match = names.__next__()

if not match:
  print("No Match")
else:
  print(match)

lines = re.split(r"\n", "Beautiful is better than ugly.\nExplcit is better than implicit")
print(lines)

pattern = re.compile(r"\W") # matches any non alpha numeric character
words = pattern.split("Drag racing is is a drag")
print("re.split(r'\W', 'Drag racing is is a drag'): ", words)


# the following method only splits up to an integer given and then
# outputs the rest of the string in the last position of the list
# e.g.
words = pattern.split("Drag racing is is a drag", 2)
print("re.split(r'\W', 'Drag racing is is a drag', 2): ", words)

# split, in addition to the split strings, never returns the character with which to
# split, unless groups are used.
# For example:
greet="Hello-World"
pattern = re.compile(r"(-)")
words = pattern.split(greet)
print(words)

"""
Note that when a group matches the start of the string, the result will contain the
empty string as a first result.
A group is returned when () is used
So pattern.split("hello-word") will result in ['hello', '-', 'world']
whereas
pattern.split(" hello-word") will result in ['', 'hello', '-', 'world']
Note the space in front of hello, whereas the previous example had no space.
"""
