#!/usr/bin/python3
"""
Refer to discussion in formatting_template_example.py before reading about format conversions.

A format rule is applied as {substitute_name:format} over a placeholder. 
The format function substitutes the variable name passed to it into the placeholder.

A {substitute_name!conversion} is also available for use.
The 3 conversions available are:
    {substitute_name!r} = outputs repr(substitute_name)
    {substitute_name!s} = output str(substitute_name)
    {substitute_name!a} = output ascii(substitute_name)

"""

print(__doc__)

some_integer = 10
some_string = "Hello World"

# The mapping between place holder and variable can be done manually by specifying the place holder name = variable name
print("{some_integer!r} {some_string!r} ".format(some_integer=some_integer, some_string=some_string))

# Place holder position numbers can also be used, instead of place holder names
# in which case the mapping (place holder name = variable name) need not be specified
print("{0!r} {1!r} ".format(some_integer, some_string))

# 
# Or, from Python 3.6 one can use f strings, where a variable can be placed within a quoted
# string
print(f"{some_integer!r} {some_string!r}")

