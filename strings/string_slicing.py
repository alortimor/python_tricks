#!/usr/bin/python3
"""

There is no difference in the parameters and 
return values (in the case of positive outcomes) between string.find() and string.index().
The difference lies in that index generates a ValueError and find returns -1 when the
string is not found.

"""
print(__doc__)

title = "Recipe 5: Rewriting, and the Immutable String"
colon_position = title.find(':')
print("Sample text is {} ".format(title))

print("title.index(':') is {} and title.find(':') is {} ".format(title.index(':'), title.find(':')))

print("discard_text, post_colon_text =title[:colon_position],title[colon_position+2:]")

discard_text, post_colon_text =title[:colon_position],title[colon_position+2:]

print("discard_text is '{}', post_colon_text is '{}' = title[:colon_position],title[colon_position+2:]".format(discard_text, post_colon_text ))

print("title[-1] is the last character: {} ".format(title[-1]))
print("title[-2] is the next to last character: {} ".format(title[-2]))
print("title[-6:] is the last six characters: {} ".format(title[-6:]))

