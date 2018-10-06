#!/home/bluefrog/anaconda3/bin/python3
"""

add 2 lists together using either '+' or extend().
Use insert() to insert an element at a specific position within the list
"""

import pathlib

rootdir = pathlib.Path("/home/bluefrog/sample_code/python")
file_list = []
print("Present working directory : {}/n".format(pathlib.Path.cwd()))
# all python files under the python/numbering directory
python_files_numbering = [(p, p.stat().st_size) for p in rootdir.glob("**/numbering/*.py")]
# all python files under the python/regular_expressions directory
python_files_regular_expressions = [(p, p.stat().st_size) for p in rootdir.glob("**/regular_expressions/*.py")]

file_list = python_files_numbering + python_files_regular_expressions

print("File list count {} ".format(len(file_list)))

# print complete file list
#for p in file_list:
#  print("{}".format(p))

# another way to add 2 lists is to use either extend or append, for example:
file_list = []
file_list = python_files_numbering 
print("File list count before extend {}".format(len(file_list)))
file_list.extend(python_files_regular_expressions)
print("File list count after extend {}".format(len(file_list)))

# use insert to place an element at a specific position within a list,
# for example the following insert() places the second list at position 0
file_list = []
file_list = python_files_numbering
print("File list count before insert {}".format(len(file_list)))
file_list.insert(0, python_files_regular_expressions)
print("File list count after insert {}".format(len(file_list)))
