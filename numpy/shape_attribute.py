#!/usr/bin/python3

"""
The shape attribute, array attribute, outputs dimensions of an array as a tuple.
For example, for a two dimenional array tha tuple would be (n,m).
For a one dimensional the tuple would be in the form (n,).

For a 2x4 dimenional array, the tuple would be (2,4).
Note, if at least one of the elements is a float, then all all elements are considered float.
the following is an array of integers:
    [0,1,55,99]
the following is an array of float:
    [0,1, 55., 99]

Tou can convert a Python list to a numpy array, for example:
    some_list = [0,1,2,3]
    some_list = np.array(some_list)

One can explicitly assign a specific data type to all elements of an array, for example:
    a = np.arange(10, dtype=uint16)
or
    array([0,1,2,3], dtype=uint16)

Type      Description
====      ===========
bool      Boolean (True or False) stored as a bit
inti      Platform integer (normally either int32or int64)
int8      Byte (-128 to 127)
int16     Integer(-32768 to 32767)
int32     Integer(-2 ** 31 to 2 ** 31 -1)
int64     Integer(-2 ** 33 to 2 ** 31 -1)
uint8     Unsigned intgege (0 to 255)
uint16    Unsigned integer (0 to 65535)
float16   Half precision float: sign bit, 5 bits exponent, 10 bits mantissa
float32   Single precision float: sign bit, 8 bits exponent, 23 bits mantissa
float64 or float Double precision float: sign bit, 11 bits exponent, 52 bits mantissa

complex64  Complex number, represented by two 32 bit floats (real and imaginary components)
complex127 Complex number, represented by two 64 bit floats (real and imaginary components)

A listing of all data types names and how to declare them is available with :
    np.sctypeDict.keys()
"""
print(__doc__)
import numpy as np

# One dimensional array of 10 elements
print("One-dimensional sample array {}".format(np.arange(10)))
print("Array shape {} ".format(np.arange(10).reshape(2,5).shape))

# You can convert a Python list to a numpy array:
some_list = [0,10,20,30,40,50,60,70,80,90]
some_list = np.array(some_list)
print("Numpy array converted from a python list: {}".format(some_list))
print("Data type of numpy array converted from a python list: {}".format(some_list.dtype))

a = np.arange(10)
a = a.reshape(2,5)
print("Shape (a.shape[0] of a two by five dimension array: {}".format(a.shape[0])) # equivalent to n
print("Shape (a.shape[1] of a two by five dimension array: {}".format(a.shape[1])) # equivalent to m
print("Shape (a.shape) of a two dimensional array: {} ".format(a.shape))

a3d = np.arange(24).reshape(3,4,2)
print("Shape of a three dimensional array: {}".format(a3d.shape))

# One can explicitly cast an entire arrays elements to a different type, for example:
a = np.arange(10).reshape(2,5)
print("Integer array\n{}".format(a))
print("Integer array cast to float\n{}".format(a.astype('f8')))

# One can prevent the array from being copied in memory when being casted with astype by setting copy=False, for example:
print("Float array cast back to integer\n{}".format(a.astype('uint16', copy=False)))

print("Full list of Numpy data types and their key can\n\
be obtained with the np.sctypeDict.keys()")

print(
"Key:       Value\n\
==================")

for k,v in np.sctypeDict.items():
    print(f"{k}:\t\t{v}")


