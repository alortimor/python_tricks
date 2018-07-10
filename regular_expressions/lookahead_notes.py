#!/usr/bin/python3
import re

"""
Positive look ahead "?="
=======================
(?=regex) will match if the regex matches the input that follows.

Negative look ahead "?!"
=======================
(?!regex) will match if the regex does NOT match the input that follows.

Positive look behind "?<="
=========================
(?<=regex) will match if the regex does match against the previous input.

Negative look behind "?<="
=========================
(?<!regex) will match if the regex does NOT match against the previous input.

"""

text = "The quick brown fox jumps over the lazy dog"

# no look ahead
pattern = re.compile(r'fox')
result = pattern.search(text)
print("Start ", result.start(), " End ", result.end())

# with look ahead
pattern = re.compile(r'(?=fox)')
result  = pattern.search(text)
print("Start ", result.start(), " End ", result.end())

"""
The result for the first search is 16 and 19.
The result in the second search is 16 and 16.

The reason the start and end are the same for the 2nd search
is because the look around does not consume characters.
It can therefore be used to verify a start position for consumption ahead.

"""
