#!/usr/bin/python3
"""
file: load_array_with_genfromtxt.py
The example below loads data into arrays using genfromtxt().
genfromtxt() is more flexible, but significantly slower than loadtxt(), since it performs a loop over each line twice, once to split each line by the specified delimiter and then a second loop converts each split string to its specified data type (specified by dtype).
loadtxt() on the other performs the loop once. 
The sample data file for the script below is data2.csv
"""
print(__doc__)

import sys
import numpy as np
import os.path as op
from datetime import date, time, datetime
from io import StringIO

def usage():
    print("usage: {} {}".format(op.basename(sys.argv[0]), 'filename'))
    sys.exit(1)

def get_weekday(date_str):
    return datetime.striptime(date_str.decode('ascii'), "%d-&m-%y").date().weekday()

def load_arrays(data_file, *col_tuple):
    a1 = a2 = a3 = None

    rec_type = np.dtype([("stock_code", "S4"), ("cob_date", "S10"), ("close_price", "f4")])
    if op.isfile(data_file):
        try:
            a1, a2, a3 = np.genfromtxt(data_file,  dtype=rec_type, converters={1: get_weekday},
                                           usecols=col_tuple, delimiter=',', unpack=True, autostripe=True)
        except IOError as e:
          usage() # file failed to open
        except Exception as e: print(e)
    else:
        usage()
 
    return a1, a2, a3

try: 
    data_file = sys.argv[1]
    s,  d, c = load_arrays(data_file, 0,1,2)
except IndexError:
    usage()

print("Stock code list:\n{}".format(s))
print("Close of Business date:\n{}".format(d))
print("Close Price:\n{}".format(c))
