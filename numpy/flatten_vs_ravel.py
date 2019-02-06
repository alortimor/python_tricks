#!/usr/bin/python3

"""
Multi-dimensional numpy arrays often require flattening.
ravel() generates a flattened copy only when needed, whereas flatten() creates a copy of the array regardless.
ravel() returns a view of the original whenever possible.
If you modify the array returned by ravel, it will modify the entries in the original array.
The converse is true for flatten().

ravel() will work on any object that is successfully parsed, e.g. list of ndarrays, while flatten,
since it is a method of method of an ndarray object, can only be called for true numpy arrays.

ravel() will often perform better in the assignment since no memory is used.
flatten() will perform better if many subsequent mutations are required.
flatten() is safer, since the original is guranteed not to be modified, but uses more memory.

If no modifications are planned then ravel() is preferred.

Example of flattening a multi-dimensional array, from a 3 dimensional
to a 2 dimensional.
Given a 3 dimensional array such as:  a = np.arange(24).reshape(2,3,4)
[
 [
   [ 0,  1,  2,  3],
   [ 4,  5,  6,  7],
   [ 8,  9, 10, 11]
 ],
 [
   [12, 13, 14, 15],
   [16, 17, 18, 19],
   [20, 21, 22, 23]
 ]
]

one can flatten to a 2 dimensional array:
    a.reshape(3,8)
Note, the overall count of elements remained the same, i.e. 24 elements

If a dimension is specified that amounts to a lower number of elements, then a ValueError will
occur, since reshape cannot accommodate all elements, for example:
    a.reshape(2,6)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: cannot reshape array of size 24 into shape (2,6)

Notes:
    - reshape mutates an array without modifying data
    - It is not always possible to to modify the shape of an array without copying the data.
    - reshaping using reshape() or (..) isoften used in Linear Algebra matrix transformations

for example:
  a = np.arange(24).reshape(2,3,4), which is depicted 

a.reshape(6,4)
[
  [ 0,  1,  2,  3],
  [ 4,  5,  6,  7],
  [ 8,  9, 10, 11],
  [12, 13, 14, 15],
  [16, 17, 18, 19],
  [20, 21, 22, 23]
]
Note, the elements have not been modified, but the shape and dimension of the array has.

Transpose is a function that will take an input a two-dimensional vector (or square if you like)
and flip the matrix by its columns to rows (or vice-versa)

for example, a.transpose() will output:
    [
     [ 0,  4,  8, 12, 16, 20],
     [ 1,  5,  9, 13, 17, 21],
     [ 2,  6, 10, 14, 18, 22],
     [ 3,  7, 11, 15, 19, 23]
    ]
Note, instead of a.transpose() one can use a.T

transpose() can be used to reshape an array using a tuple of axis
related to the number of dimensions, for example:
given
  a = np.ones(12).reshape(2,2,3)
[
 [
  [1., 1., 1.],
  [1., 1., 1.]
 ],
 [
  [1., 1., 1.],
  [1., 1., 1.]
 ]
]

a.transpose( (2,0,1) )
[
 [
   [1., 1.],
   [1., 1.]
  ],
  [
   [1., 1.],
   [1., 1.]
  ],
  [
   [1., 1.],
   [1., 1.]
  ]
]
the integers (2,0,1) relate to the position of the dimension, the dimensions were shaped as (2,2,3),
but were transposed to (3,2,2) based on (2,0,1)
"""
print(__doc__)
import numpy as np

b = np.arange(24).reshape(2,3,4)
print("Three dimensional array:\n{}".format(b))
print("Three dimensional array flattened into a view with ravel():\n{}".format(b.ravel()))
c = b.flatten()
print("Three dimensional array flattened with flatten():\n{}".format(c))
print("Two dimensional array reshaped and transposed in one line:\n{}".format(b.reshape(6,4).transpose() ))
