#!/usr/bin/python3
"""

When pressing enter instead of entering a name, the following error occurs:
    Please enter your name:
Traceback (most recent call last):
  File "./get_first_name.py", line 17, in <module>
    first_name = get_first_name(fallback_name)
  File "./get_first_name.py", line 5, in get_first_name
    return full_name.split(" ")[0]
AttributeError: 'dict' object has no attribute 'split'

With type hinting, the error is caught prior to running by using mypy from the command line as follows:
$ mypy get_first_name.py
test.py:16: error: Argument 1 to "get_first_name" has incompatible type Dict[str, str]; expected "str"

"""
print(__doc__)
from typing import Dict

def get_first_name(full_name: str) -> str:
    return full_name.split(" ")[0]

fallback_name: Dict[str, str] = {
    "first_name": "UserFirstName",
    "last_name": "UserLastName"
}

raw_name: str = input("Please enter your name: ")
first_name: str = get_first_name(raw_name)

# If the user didn't type anything in, use the fallback name
if not first_name:
    first_name = get_first_name(fallback_name)

print(f"Hi, {first_name}!")
