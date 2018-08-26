#!/usr/bin/python3
"""
Generally exceptions that occur with :
    SystemError
    RuntimeError
    MemoryError
should not be handled, since attempting to handle them will cause unexpected behaviour
with the host operating system
For example, when pressing Ctrl-C on the unix termnial should send a SIGINT and the
process should be killed as a result.

Do not specify exception without an exception class, since this will match all exception classes.

Finally, avoid catching:
    SystemExit
    KeyboardInterrupt
    GeneratorExit

Generally, attempting to handle Python's internal exceptions will hide an obvious exception
and therefore obstruct fixing the problem, since the real problem is less clear.
"""

print(__doc__)
