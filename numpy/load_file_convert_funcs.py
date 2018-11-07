#!/home/bluefrog/anaconda3/bin/python3

import sys
import numpy as np
import os.path as op
from datetime import datetime, date, time
from io import StringIO

sample_data = StringIO(
"AAPL,28-01-2011,344.17,344.4\n\
AAPL,31-01-2011,335.8,340.04\n\
AAPL,01-02-2011,341.3,345.65\n\
AAPL,02-02-2011,344.45,345.25\n\
AAPL,03-02-2011,343.8,344.24\n\
AAPL,04-02-2011,343.61,346.7")

def usage():
    print("usage: {} {}".format(op.basename(sys.argv[0], 'filename')))

def get_weekday(date_str):
    return datetime.strptime(date_str.decode('ascii'), "%d-%m-%Y").date().weekday()

def load_arrays(data_file, *col_tuple):
    a1 = a2 = None

    try:
        a1, a2 = np.loadtxt(data_file, 
                                dtype={'names': ('stock_code','high_price'),
                                       'formats': ('S4', 'f4')}, 
                                converters={1: get_weekday}, delimiter=',',
                                usecols=(0,2), unpack=True)

    except IOError as e:
        usage() # failed to open file
    except Exception as e: print(e)

    return a1, a2

try:
    data_file = sample_data
    s,  h= load_arrays(data_file)
except IndexError:
    usage()

print("Stock code array:\n{}".format(s))
#print("\nClose of Business date array:\n{}".format(d))
print("\nHigh price array:\n{}".format(h))
#print("\nLow price array:\n{}".format(l))

