#!/home/bluefrog/anaconda3/bin/python3
"""
file: basic_stat_functions.py
Weighted averages in numpy can be obtained with the average function.
The mean is the average where the weight is defaulted to 1.

Highest and lowest values can be obtained using np.max() andnp.min()
The spread of an array, i.e. max() - min(), can be output with np.ptp()

mean is calculated by adding all elements and then dividing by the array size.
median is obtained by sorting the array and then identifying the 'middle' element.
"""
print(__doc__)
import sys
import numpy as np
import os.path as op

def usage():
    print("usage: {} {}".format(op.basename(sys.argv[0], 'filename')))
    sys.exit(1)

def get_weekday(date_str):
    return datetime.strptime(date_str.decode('ascii'), "%d-%m-%Y").date().weekday()

def load_arrays(data_file, *col_tuple):
    a1 = a2 = None

    if op.isfile(data_file):
        try:
            a1, a2 = np.loadtxt(data_file, 
                                converters={1: get_weekday}, delimiter=',',
                                usecols=col_tuple, unpack=True)

        except IOError as e:
            usage() # failed to open file
        except Exception as e: print(e)
    else:
        usage()

    return a1, a2

try:
    data_file = sys.argv[1]
    c, v = load_arrays(data_file, 6, 7)
except IndexError:
    usage()

print("Arrays as a result of loading data from {}".format(data_file))
print("Closing price\n{}\n".format(c))
print("Trade Volumes\n{}\n".format(v))

vwap = np.average(c, weights=v)
print("Volume wieghted average {}".format(vwap))
print("The difference between numpy's mean and average is that the latter can take an\n\
array of weightings as an additional parameter, so that averages such as\n\
weighted volumes or time can be output")
print("Mean of prices: {}".format(np.mean(c)))
print("Highest cloing price: {}".format(np.max(c)))
print("Lowest closing price: {}".format(np.min(c)))

h, l = load_arrays(data_file, 4, 5)
print("High price spread: {}".format(np.ptp(h)))
print("Low price spread: {}".format(np.ptp(l)))

print("\nThe median of an array that has an odd number of elements is always the middle, e.g. 4 for size 7.\n\
However, for even sized arrays the median is calculated by adding the 2 middle elements and dividing by 2,\n\
i.e. (Assume A is a sorted array) ( A[size / 2] + A[ (size - 1)/2 ] ) / 2")

a = np.array([1,3,5,5,7,9,9])
b = np.array([1,3,4,5,7,9])

print("\nThe median of an odd sized {} array: {}".format(a, np.median(a)))
print("\nMedian of an even sized {} array: {}".format(b, np.median(b)))

print("\nTo sort an array use np.msort(). msort() returns a copy of the array, so as to leave the original order as is")
print("Sorted closing prices:\n{}".format(np.msort(c)))
print("\nThe variance of closing prices is obtained with np.var() : {}".format(np.var(c)))

print("\nDifferentiation within the closing price array:\n{}".format(np.diff(c)))
print("\nAssuming each closing price represents a return on a previous closing price, np.diff().\n\
represents a 'return', for example a return on a closing price of [4.1, 7.2, 11] is [3.1, 3.8],\n\
hence np.diff(array) / array[:-1] represents the ratios of returns over the 'investment', which is in effect the opening\n\
price, since the previous closing price is the current day opening")

returns = np.diff(c) / c[:-1]
print("Returns for closing :\n{}".format(returns))

print("\nThe logarithm (np.log(array)) of each element in the closing price:\n{}".format(np.log(c)))
print("\nThe logarithm of the differences for the closing price array, i.e. np.diff(np.log(c)):\n{}".format(np.diff(np.log(c))))
print("\nStandard deviation calculated with np.std(c): {}".format(np.std(c)))

print("\nThe logarithmic returns for each element is useful for obtaining an indication of volatility\n\
over a time series.\n\
To determine a yearly volatility for the closing price, the steps involved are:\n\
a. Obtain the derivative of the log of the closing price for each element\n\
b. Obtain standard deviation of the log for each element, based on the output from a\n\
c. Obtain the mean of the log for log returns obtained in step a.\n\
d. Calcualte the ratio of the above (b / c) for each element\n\
e. Calculate the yearly volatility as follows y ÷ (1 ÷ √x) (y = result from d, x = number of days)")

logreturns = np.diff(np.log(c))
std_lr = np.std(logreturns)
mean_lr = np.mean(logreturns)

yearly_volatility = np.std(c)

wd = 252. # assume 252 working days in a year
print("calculate d first:\n{}".format(std_lr/mean_lr))
# when dividing ensure dividend and divisor are both float or else numerical inaccuracies can occur
print("Calculate e next:\n{}".format( (std_lr/mean_lr) / np.sqrt(1./wd )))

print("\nA WHERE clause can be applied to array to filter elements based on a specific criteria\n\
for example: np.where(array > 0) will output positive elements")

print("\nDifferentiations greater than zero using a.where:\n{}".format(np.where(np.diff(c) >0)))

