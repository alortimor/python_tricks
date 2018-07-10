#!/usr/bin/python3
import re


pattern = re.compile (r'(a|b)+')
list = pattern.findall('aba')
print("Result using r'(a|b)+' on 'aba' :", list)


"""
(a|b)+ will be a repeated capturing group due to the "+", and only capture the last iteration.
So it matches the last a.
Remove + to capture all characters. In addition the () can be removed.

So the RE '(a|b)+' applied over the string 'aba' produces the following sequence:
- Applied from char 0: Match 'aba'
- Applied from char 1: Match 'ba', so the previous match is discarded
- Applied from char 2: Match 's' and the previous match is discarded.
So it is not returning the 1st 'a' but the last... you can check it with re.findall(r'(a|b|c)+', 'abc') that returns ['c']
"""

# So the trick is to 
pattern = re.compile (r'(a|b)+?')
list = pattern.findall('aba')
print("Result using r'(a|b)+?' on 'aba' :", list)
"""
>>> re.findall(r'(a|b)+?', 'aba')
['a', 'b', 'a']
>>> re.findall(r'[ab]', 'aba')
['a', 'b', 'a']
>>> re.findall(r'(a|b)', 'aba')

"""


pattern = re.compile(r'[ab]+')
list = pattern.findall('aba')
print("\nResult using r'[ab]+' on 'aba' :", list)

"""
If you want to capture the groups made of
several 'a' or 'b' in any order, for example on a string like 'abbaca'.
The following expression does the trick:
r'((?:a|b)+)', 
['abba', 'a']
Captures every group made up of the subexpression (a|b) and not to group just one character.

"""
pattern = re.compile(r'((?:a|b)+)')
list = pattern.findall('abbca')
print("\nResult using r'((?:a|b)+)' on 'abaca' :", list)

