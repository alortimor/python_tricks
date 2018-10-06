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

# the following returns a single value, since a an indexing method was used
print("First item : {} ".format(stock_items[0]))
# the folowing however returns a list due to a slicing method being used
print("last item : {} ".format(stock_items[-1:]))

print("First item, and then every 3rd item {} ".format(stock_items[0::3]))
print("Second item, and then every 3rd item {} ".format(stock_items[1::3]))

print("Two lists zipped : {} ".format(list(zip(stock_items[0::3], stock_items[1:3]))))
