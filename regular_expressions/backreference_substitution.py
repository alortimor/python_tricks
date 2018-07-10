#!/usr/bin/python3
import re

text = "Follow up on the new sales *order*. Do not consider the cancelled *order*"
pattern = re.compile(r'\*(.*?)\*')

"""
The difference between .* and .*? is that the latter prevents a greedy search,
since the addition of the ? prevents a continuation of the match.
For example, the regular expression ".*" will match Hello and Hola
"Hello hola"
whereas ".*?" will only match the first word, i.e. "Hello", since ? limits
the match to 0 or 1.
"""

# the following uses a regular expression to perform the substitution
# using a pattern compiled

## the \g<number> notation is used todenote a group in a backreference

print("Before substitution: ", text)
text = pattern.sub(r"<b>\g<1><\\b>", text)
print("After substitution: ", text)

"""
the following code generates an error

text = "Follow up on the new sales *order*. Do not consider the cancelled *order*"
pattern = re.compile(r'\*(.*?)\*')
print("Before substitution: ", text)
transform_pattern = re.compile(r"<b>\g<1><\\b>")
text = pattern.sub(transform_pattern, text)
print("After substitution: ", text)

"""
