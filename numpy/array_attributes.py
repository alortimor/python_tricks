#!/usr/bin/python3
"""
Numpy arrays have several attributes and methods that can be used to obtain information and effect change.
Numpy arrays are generally created with np.array. 'zeros', 'ones' & 'empty' are convenient methods
to initialise numpy arrays.
You can also use np.ndarray, but it is not recommended (as per ndarray docstring)

The following is a short summry of attributes:
    array.ndim = number of dimensions
    array.size = number of elements
    array.dtype = data type of the array
    array.itemsize = number of bytes per element
    array.nbytes = total number of bytes consumed by the array ( ≈ array.size * array.itemsize )

    array.astype is used to typecast elements, for example:
    a np.array([1. + 1.j, 2. + 1.j]) is an array of complex numbers
    a.astype(int) will cast the array to integer, but the imaginary numbers are not included.
    only the real numbers are cast.

You can convert a numpy array to a Pyhton list using tolist(), for example
  b = [1.+1.j, 3.+2.j]
  b.tolist()

There are attributes that exist to obtain information on complex numbers, for example:
  a = np.array([[1. + 1.j, 2. + 1.j, 3. + 1.j]
  a.real
  array([ 1., 2., 3. ])
  a.imag
  array([ 1., 1., 1. ])

For arrays with complex numbers as elements, the data type of the array will be complex, for example:
    a.dtype
    dtype('complex128')

Other useful array creation methods are eye and identity (both create 2 dimensional arrays).
eye creates an array of zeros, with ones across a diagonal (start at specified index - default 0)
for example, the following is a 2 dim array (3x3) of zeros with the diagonal at 0.
[1, 0, 0]
[0, 1, 0]
[0, 0, 1]

Another example is np.eye(4,5,2,dtype=int) # (rows, columns, diagonal_start, data_type)
which will result in:
[
  [0, 0, 1, 0, 0],
  [0, 0, 0, 1, 0],
  [0, 0, 0, 0, 1],
  [0, 0, 0, 0, 0]
]

The difference between eye and identify is that a single integer denotes both columns and rows
with identify, so a square is always output, e.g.
e = np.identify(3, dtype=int)
[
  [1, 0, 0],
  [0, 1, 0],
  [0, 0, 1]
]
e = np.identify(4, dtype=int)
[
  [1, 0, 0, 0],
  [0, 1, 0, 0],
  [0, 0, 1, 0]
  [0, 0, 0, 1]
]
"""
print(__doc__)
import numpy as np
a = np.array([1. + 1.j, 2. + 1.j, 3. + 1.j])
print("\nSample array with complex numbers as elements:\n{}".format(a))
print("\nThe imaginary part of the complex array:\n{}".format(a.imag))
print("\nThe real part of the complex array:\n{}".format(a.real))
print("\nThe data type string, based on a.dtype:\n{}".format(a.dtype))

