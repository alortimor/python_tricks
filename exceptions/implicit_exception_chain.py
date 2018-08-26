#!/usr/bin/python3
"""

Chaining is generally useful when more detailed exceptions are required for code that
is less abstractor or where logging is required at a deatiled level.

A quote from PEP-3134
'exceptions are composed of three parts: the type, the value, and the traceback.
The sys module, exposes the current exception in three parallel variables:
    exc_type
    exc_value
    exc_traceback

The sys.exc_info() function returns a tuple of these three parts.
The raise statement has a three-argument form accepting these three parts.'

Implicit Exceptions:
====================
__context__ attribute is used for implicitly chained exceptions. 
The __context__ attribute retains the information about the chain of exceptions.
__context__ is used, since if progressing the current exception, another was raised while trying to handle the current.
__context__ refers to the exception that was being handled at the time the other exception was raised. 
This facilitates implicit chaining, meaning the original exception is not lost because another exception occurred.

Adding __traceback__ attribute to exception values makes all the exception information accessible from a single place

Python sets a context on exceptions so you can introspect where an exception was raised, 
letting you see if another exception was replaced by it. 
You can also add a cause to an exception, making the traceback explicit about the
other exception (use different wording), and the context is
ignored (but can still be introspected when debugging). 
Using raise ... from None lets you suppress the context being printed.
"""

print(__doc__)

def main(filename):
  file = open(filename)       # oops, forgot the 'w'
  try:
    try:
      compute()
    except Exception as exc:
      log(file, exc)
  finally:
    file.clos()         # oops, misspelled 'close'

def compute():
  1/0

def log(file, exc):
  try:
    print >>file, exc       # oops, file is not writable
  except:
    display(exc)

def display(exc):
  print(ex)                    # oops, misspelled 'exc'

main('t.txt')

