#!/home/bluefrog/anaconda3/bin/python3
"""
Shows how to do list slicing.
Reads from a file, stock_list.dat. The following is a sample of the data in the file:
Dairy, Butter, 30
Fruit, Apples, 500
Fruit, Oranges, 500
"""

from pathlib import Path
import csv

rootdir = Path("/home/bluefrog/sample_code/python/lists")
print("Present working directory : {}/n".format(Path.cwd()))

# Read the data file into a list
with Path("stock_list.dat").open() as stock_file:
    read_rows = csv.reader(stock_file)
    stock_items = list(read_rows)

print("Stock items : {} ".format(stock_items))

# the following returns a single value, since an indexing method was used
print("First item : {} ".format(stock_items[0]))
# the folowing however returns a list due to a slicing method being used
print("last item : {} ".format(stock_items[-1:]))

print("First item, and then every 3rd item {} ".format(stock_items[0::3]))
print("Second item, and then every 3rd item {} ".format(stock_items[1::3]))

# Purpose of zip() is to map similar index of several containers so that they can be used as a single entity.
print("Two lists zipped : {} ".format(list(zip(stock_items[0::3], stock_items[1:3]))))

list_copy = stock_items[:]
print ("Copy of list using [:] : {} ".format(list_copy))

# Instead of [:] one can also specify list_copy = list.copy() to make a copy of a list
list_copy = stock_items.copy()
print ("\nCopy of list using copy() : {} ".format(list_copy))

# "del" can delete all elements in a list or part of a list with slicing, for example:
# In addition, del can also remove an item at a specific index
del list_copy[:2]
print ("\nList after del[:2] : {} ".format(list_copy))

# remove differs from del in that it performs a match, based on the parameter passed to the remove() function
list_copy.remove(list_copy[0])
print("First element removed : {} ".format(list_copy))

# pop() can also be used to remove an item. pop() only takes an integer however, unlike remove()
# Also, pop() returns the value of the element removed, whereas remove does not.

# pop without any integer parameter removes the last item in the list
item_removed = list_copy.pop()

print("First element removed : {} ".format(list_copy))
print ("Item removed : {} ".format(item_removed))


