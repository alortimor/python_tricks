#!/usr/bin/python3

import re
import sys

if __name__ == "__main__":
  search_string = sys.argv[1]
  # compiled_re = re.compile('^[a-zA-Z.]+@([a-z.]*\.[a-z]+)$')
  match = re.match('^[a-zA-Z_.1-9]+@([a-z.]*\.[a-z]+)$', search_string)

  if match:
    domain = match.groups()
    print(domain)
  else:
    print("Not a valid email")
  
