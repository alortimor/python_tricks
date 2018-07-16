#!/usr/bin/python3

import re
import sys

if __name__ == "__main__":
  pattern = sys.argv[1]
  search_string = sys.argv[2]
  compiled_re = re.compile(pattern)
  match = compiled_re.match(search_string)

  if match:
    template = "'{}' matches pattern '{}'"
  else:
    template = "'{}' does not match pattern '{}'"

  print(template.format(search_string, pattern))
