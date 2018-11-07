#!/usr/bin/python3

"""
Numpy arrays can be sliced inthe same way as python strings and arays.  
There are a few tricks to observe for multi-dimensional arrays though. 

Thisnk of b = np.arrange(24), reshape(2,3,4) as a building of 2 floors of 3 corridors, where each corridor has 4 rooms. 

For strings, by ommitting an index and specifying a leading colon(:), the output is up to, but not including, for example x="abcdefg"
So x[:2] outputs 'ab'

Conversely, a trailing colon (:) outputs from and also including the index, so x[2:] would output 'cdefg'

Slicing with multi-dimensional arrays is somewhat similar:
For example, by omitting a dimension, but including others, the output would be for each dimention that is ommitted. 
For example, assuming b hold the following:
	[[[ 0,  1,  2,  3],
	    [ 4,  5,  6,  7],
            [ 8,  9,  10,  11]],

	   [[12, 13,  14,  15],
	    [16, 17,  18,  19],
	    [20, 21,  22,  23]]]

So, b[1,1:], would output the 2nd floor and all corridors apart from the fist corridor:
   array ([[16, 17, 18, 19],
          [20, 21, 22, 23]])

So, b[1,1:,0], would output the 2nd floor and all corridors apart from the first corridor, and only the first room for each corridor 
   array([16,20])

The important thing to rmember is that dimensions are separated by commas, whereas slices are specified by a colon(:) within a dimension, so [:,:,:] would be an adequate representaion I guess. 

One more syntax issue to be aware of is the use of an elipses:
Multiple colons(:), can instead be replaced by an elipses, so b[0, :, :] can also be coded as b[0, ...]

both output :
    array ([[ 0, 1, 2, 3],
       [ 4, 5, 6, 7],
       [ 8, 9, 10,11]])
"""
print(__doc__)
import numpy as np

a = np.arange(18)
print("Sample numpy array arange(18) {}".format(a))
print("Sample numpy array arange(18) sliced as array[4:8]. {}".format(a[4:8]))
print("Sample numpy array arange(18) in reverse using np.arange(18)[::-1] : {} ".format(np.arange(18)[::-1]))

print("The same applies to multi-dimensional arrays, for example")
b = np.arange(24).reshape(2,3,4)
print("For a 3-dimensional array b = np.arange(24).reshape(2,3,4)\n {} ".format( b))

print("\nnp.arange(24).reshape(2,3,4)[:,0,0] will show both 3rd dimension levels,\n\
but only 1st element of leve 2 (which is a 2 dimensional array) and only the first element of\n\
the lowest level {}".format(np.arange(24).reshape(2,3,4)[:,0,0]))

print("\nnp.arange(24).reshape(2,3,4)[0,1:] will show all elements\n\
of the 2nd 2nd level of the lowest level  {}".format(np.arange(24).reshape(2,3,4)[0,1,:]))

print("\nnp.arange(24).reshape(2,3,4)[0, :, :] will show all elements\n\
in the t 3rd dimension {}".format(np.arange(24).reshape(2,3,4)[0, : , :]))

print("\nnp.arange(24).reshape(2,3,4)[0, ...] will show the same elements\n\
as previously, except that elipsis (...) replaces all colons {}".format(np.arange(24).reshape(2,3,4)[0, ...]))










