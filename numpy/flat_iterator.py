#!/usr/bin/python3

"""
Numpy arrays can be interated over with an interator object, which is assigned from the flat method: 
	a = np.arange(1,9).reshape(2,4)
	[
	 [1,2,3,4],
	 [5,6,7,8]
	]
	f = a.flat
	f is now an iterator object:
	<numpy.flatiter object at 0x60047c2d0>

	which can only be iterated over once!

	It is also possible to target specific elements to iterate over:
	f = a.flat[ [1,3,6]]

	setting the flat attribute results in all elements being replaced by the set value, for example 
	a = np.arange(1,3)
	[1,2,3]
	
	a.flat = 1 results in 
	[1,1,1]

"""
print(__doc__)
import numpy as np
