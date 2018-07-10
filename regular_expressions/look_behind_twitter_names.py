#!/usr/bin/python3
"""
Twitter username restrictions:
Username can only contain alphanumeric characters (letters A-Z, numbers 0-9)
with the exception of underscores. Username may not contain symbols, dashes, or spaces.

For example:

@xyz - valid user name
@xyz_abc - valid user name, since underscores are allowed
@xyz!abc - invalid user name, since special characters are not allowed
@xyz abc - invalid user name, since spaces are not allowed
@999 - valid username
"""
import re

text = "Know your Big Data = 5 for $50 on eBooks and 40% \
off all eBooks until Friday #bigdata #hadoop @HadoopNews packtpub.com \
bigdataoffers"

print(__doc__)

print("\nSample text:\n "+ text + "\n")

pattern = re.compile(r'\B@[\w_]+')
list = pattern.findall(text)

print(list)

pattern = re.compile(r'(?<=\B@)[\w_]+')
list = pattern.findall(text)

print (list)




