#!/usr/bin/python3

"""
Working with files, databases, networks can lead to memory leaks if connections are not closed
once processing is completed.
Resources are used unnecessarily . Using a context manager using the 'with' structure enables
cleaning up and closing down of any open resources.

some_text='some sample text'
target_path = pathlib.Path('/home/bluefrog/sample_code/python/t.txt')
with target_path.open('w+', newline='\n') as target_file:
    writer = csv.writer(target_file)
    for t in some_text.split():
        writer.writerow(t)

If an exception is raised within the with statement, the file is still properly closed. 
The context manager is notified of the exception. 
It can close the file and allow the exception to propagate.

A context manager is notified of two kinds of exits from the block of code:
    Normal exit with no exception
    An exception was raised
The context manager will release the executing code from external resources. 
Files can be closed. Network connections can be dropped. Database transactions
can be committed or rolled back. Locks can be released

"""
print(__doc__)
import csv
import pathlib

some_text='some sample text'
target_path = pathlib.Path('/home/bluefrog/sample_code/python/t.txt')
with target_path.open('w+', newline='\n') as target_file:
    #writer = csv.writer(target_file)
#    writer = writer(target_file)
    for t in some_text.split():
        target_file.write(t)


