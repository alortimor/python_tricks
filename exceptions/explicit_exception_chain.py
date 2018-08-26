#!/usr/bin/python3
"""
The __cause__ attribute provides an explicit way to record the direct cause of an exception.
This is useful for re-raising an exception, from within an exception.

The __cause__ is set by using the 'raise.. from ..' syntax:
    raise EXCEPTION from CAUSE

In the following code the 'raise from' will set the __cause__ attribute.
class DatabaseError(Exception):
    pass

class FileDatabase(Database):
    def __init__(self, filename):
        try:
            self.file = open(filename)
        except IOError, exc:
            raise DatabaseError('failed to open') from exc

open() raises an exception.
The problem will be reported as a DatabaseError, 
with a __cause__ attribute that reveals the IOError as the original cause.


When from is used, the __cause__ attribute is set and the message states what
the exception was directly caused by

If the from is ommitted then no __cause__ is set, but the  __context__ attribute may be set as well,
and the traceback then shows the context as when some other exception being handled.

When raising from an exception handler where the context is preferrably suppressed, then use raise ... from None to set __suppress_context__ to True.


class Error(Exception):
  pass

try:
  print('This is a very long string, but not as long as 99'[99])
except (IndexError, NameError) as exception:
  raise Error("index problem") from exception

The above code shows a chained exception.
The first exception in the Traceback message is an
IndexError exception. This is the direct cause. The second exception in the Traceback is
our generic Error exception. This is a generic summary exception, which was chained to
the original cause.

"""

print(__doc__)

class Error(Exception):
  pass

try:
  print('This is a very long string, but not as long as 99'[99])
  #print('hello world'[99])
except (IndexError, NameError) as exception:
  raise Error("index problem") from exception
