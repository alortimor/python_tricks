#!/usr/bin/python3

"""
file: array_copying.py

A numpy array is essentially described by metadata (i.e. ndim, dtype, shape, size, itemsize, nbytes).
The data is stored in a homogenous and contiguous block of memory, at a particular memory address. (data buffer).
Python data structures, such as a list, on the other hand are non-contiguous across system memory.
This is the main difference between numpy arrays and traditional Python data structures.
This difference makes numpy arrays highly efficient compared to Python data structures, since processing
a contiguous block of memory improves looping throughput and opportunities for lower level caching optimisation.

Certain operations and actions however can lead to the said blocks of memory being copied, which can lead
to inefficiencies and less than ideal outcomes.
Below are descriptions of what to look out for and what to avoid.

Performing calculations on numpy arrays may create copies of the array in memory.
Such copying may be less than ideal when performing read-only actions.

If modofications are planned subsequent to the computation, then a copy of the array would be
preferable if the original is required to be kept as is.

Two useful ways of determining array equivalence, in regard to memory allocation, is
to use the numpy __array_interface__ and numpy's array base object, the latter is the 
base object if memory is from some other object.
Note, if the memory is from the same object then base is None.

  The following is quoted from https://docs.scipy.org/doc/numpy-1.15.1/reference/arrays.interface.html
  'array-like Python objects to re-use each other’s data buffers intelligently whenever possible.
   The homogeneous N-dimensional array interface is a default mechanism for objects to share N-dimensional
   array memory and information.'

  The numpy array interface (__array_interface__) is a dictionary structure.
  The dictionary can be accessed using the standard Python key/value properties , for example:
  a = np.array([23,1,8,5,34,6,45])
  a.__array_interface__.keys()
  dict_keys(['data', 'strides', 'descr', 'typestr', 'shape', 'version'])
  a.__array_interface__.values()
  dict_values([(39898992, False), None, [('', '<i8')], '<i8', (7,), 3])
  a.__array_interface__.items()
  dict_items([('data', (39898992, False))
             ,('strides', None)
             ,('descr', [('', '<i8')])
             ,('typestr', '<i8')
             ,('shape', (7,))
             ,('version', 3)])

  The keys can be used to access a numpy array's metadata, for example
  a.__array_interface__['shape']    # outputs the shape (n,m) of the array
  a.__array_interface__['typestr']  # outputs the data type of the elements in a string format 
  a.__array_interface__['version']  # outputs version of the interface, latest is version 3
  a.__array_interface__['data']  # outputs a tuple (x, y), where
                                    x: pointer to the 1st element 
                                    y: True (default) or False depending whether data is read-only or not.

Reshaping a 2D array generally does not create a copy in memory, unless the array is transposed, i.e.
a.reshape() vs a.T.reshape()
"""

print(__doc__)
import numpy as np

def array_base_address(a):
    return a.__array_interface__['data'][0] # return base address

# This function obtains the base array object for a given numpy array
# Returns None if the base object is not from a different object type
def get_arr_base(arr1):
    base = arr1
    while isinstance(base.base, np.ndarray):
        base = base.base
    return base

def arr_elements_match(arr1, arr2):
    return get_arr_base(arr1) is get_arr_base(arr2)

if __name__ == "__main__":
    a = np.array([48, 3, 23, 5, 6, 25, 9, 0, 72])
    print("\nArray elements match: {}".format(arr_elements_match(a, a.copy())))
    print("Array elements match: {}".format(arr_elements_match(a, a[:1])))

    print("\nArray address matches: {}".format(array_base_address(a) == array_base_address(a.copy()) ))
    print("Array address matches: {}".format(array_base_address(a) == array_base_address(a[:1]) ))

    print("\nImplicit array copies can occur for certain calculations (e.g. a * 2), when assigned to another array,can cause a copy to be made")

    arr1 = np.array([2,6,1,45])
    b = arr1 * 2
    is_copy = array_base_address(arr1) != array_base_address(b)

    print("\nIs arr1 a copy of b = arr1 * 2 : {}".format(is_copy))

    print("\nIn-place array computations (e.g. arr *= 2) do not result in array copies.")
    memory_location_before = array_base_address(arr1)
    arr1 *= 2
    memory_location_after = array_base_address(arr1)
    is_copy = memory_location_before != memory_location_after
    print("\nIs arr1 a copy of arr *= 2: {}".format(is_copy))

    a = np.ones( (20,20))
    print("\nGiven the following 2D array [20,20] \n{}".format(a))
    b = a.reshape(5,4,20)
    print("\n2D array [20,20] reshaped to 3D [5,4,20]\n{}".format(b))
    print("\nBase adresses match despite reshaping: {}".format(array_base_address(a) == array_base_address(b)))

    x = a.T.reshape(1, -1)
    print("\nIn some cases however, base addresses do not match, (copy has occurred),\nwhen transposing & reshaping (not always), i.e. a.T.reshape(): {} ".format(array_base_address(a) == array_base_address(x)))
    print("\n{}".format(x))
    
