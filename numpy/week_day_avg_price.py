#!/usr/bin/python3
"""
Dile: week_day_avg_price.py
Working with Python and Numpy data types often resolved in the following warning:
    'FutureWarning: elementwise comparison failed; returning scalar instead, but
     in the future will perform elementwise comparison'
Thewarning is discussed in-depth in the following posting:
    https://stackoverflow.com/
"""
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
    a1 = a2 = a3 = None

    try:
        a1, a2, a3 = np.loadtxt(data_file, 
                                dtype={'names': ('stock_code','cob_date','close_price'),
                                       'formats': ('S4', 'S10', 'f4')}, 
                                converters={1: get_weekday}, delimiter=',',
                                usecols=col_tuple, unpack=True)

    except IOError as e:
        usage() # failed to open file
    except Exception as e: print(e)

    return a1, a2, a3


if __name__ == "__main__":
    try:
        data_file = sample_data
        s, d, c= load_arrays(data_file, 0,1,3)
    except IndexError:
        usage()

    print("Stock codes:\n{}".format(s))
    print("Day of the week:\n{}".format(d))
    print("Closing price:\n{}".format(c))

    x = [y.decode('utf8') for y in d]
    # np.asarray(d, dtype='uint')
    # indicies = np.where(np.array(d) == '1')
    indicies = np.where(np.array(x) == '1')
    print(f"Indicies\n{indicies}")
