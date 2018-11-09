#!/usr/bin/python3

import numpy as np

int_ones = np.ones( (3,5), dtype=np.int8)
print("Numpy array of 1's 8 bit integers {}".format(int_ones))
float_ones = np.ones( (3,5), dtype=np.float16)
print("Numpy array of 1's 16 bit floating point {}".format(int_ones))

print("Numpy data types:\n\
Type      Description\n\
====      ===========\n\
bool      Boolean (True or False) stored as a bit\n\
inti      Platform integer (normally either int32or int64)\n\
int8      Byte (-128 to 127)\n\
int16     Integer(-32768 to 32767)\n\
int32     Integer(-2 ** 31 to 2 ** 31 -1)\n\
int64     Integer(-2 ** 33 to 2 ** 31 -1)\n\
uint8     Unsigned intgege (0 to 255)\n\
uint16    Unsigned integer (0 to 65535)\n\
float16   Half precision float: sign bit, 5 bits exponent, 10 bits mantissa\n\
float32   Single precision float: sign bit, 8 bits exponent, 23 bits mantissa\n\
float64 or float Double precision float: sign bit, 11 bits exponent, 52 bits mantissa\n\
\n\
complex64  Complex number, represented by two 32 bit floats (real and imaginary components)\n\
complex127 Complex number, represented by two 64 bit floats (real and imaginary components)")

print("\nMathematically, a complex number is a number of the form A+Bi, where i is\n\
the imaginary number, equal to the square root of -1.\n\
The symbol j is used to denote a complex number,\n\
the convention being a number followed by a j representa a complex number.\n");

print("\nExplicit data type conversions can be done with castig functions; e.g.\n\
float(2) = 2.0: convert an integer to a float\n\
uint8(3.0) = 3: convert a float to an unsigned integer {} {} ".format(np.float(2), np.uint8(3.0)))

print("\nInformat on the np.dtype can be obtained with several dtype attributes\n\
dtype.char('Float64') for example will return 'f'\n\
t = np.dtype('d'), which equates to a double precision float will return the following info\n\
t.char = 'd'\n\
t.type = <class 'numpy.float64'>\n\
t.name = 'float64'\n\
t.itemsize = 8")

a = np.arange(5, dtype='f')
print("\nYou can use the single character output to define an array type, for example\n\
arange(5, dtype='f') will give you {}".format(a))

a = np.arange(5, dtype='f8')
print("\nThe number of floating bits can be specified by either 2,4 or 8,\n\
which correspond to float16, float32 and float64 respectively.\n\
For example, arange(5, dtype='f8') results in an array of five float64 elements\n\
{}".format(a))

print("\nShape of an array {} ".format(np.zeros(10, dtype='int16').shape))
print("Product of a 2 dimensional array using\n\
np.prod(np.ones((5,2), dtype='int16').shape): {} ".format(np.prod(np.ones((5,2), dtype='int16').shape)))

print("\nUse nbytes to get total bytes of all elements of an array, for example\n\
a = np.zeros(10, dtype='int16'), will be: {}\n\
a = np.zeros(10, dtype='float16'), will be: {}\n\
a = np.zeros(10, dtype='int32'), will be: {}\n\
a = np.zeros(10, dtype='float32'), will be: {}".format(np.zeros(10,dtype='int16').nbytes,
                                                       np.zeros(10,dtype='int16').nbytes,
                                                       np.zeros(10,dtype='int32').nbytes,
                                                       np.zeros(10,dtype='float32').nbytes))

