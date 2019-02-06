#!/usr/bin/pyhton3

"""
file: fancy_indexing_take.py
Fancy indexing is a technique that involves masking a list of indicies over an
array to output an array of the slots that the indicies match.
For example, given the following array [77, 4, 3, 81, 27] and a list of indicies [2, 4],
the resulting array would be [3, 27 ], since the element 2 has the value 3 and element 4 has the value 27.


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

