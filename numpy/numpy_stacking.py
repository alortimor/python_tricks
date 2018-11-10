#!/usr/bin/python3
"""
Numpy arrays can be stacked. They can be stacked in several ways:
    Assuming we have the following array:
    a = np.arange(9).reshape(3,3)
    c = np.copy(a)

Horizontal Stacking
===================
a appears as follows:
    [
     [0, 1, 2],
     [3, 4, 5],
     [6, 7, 9]
    ]
Multiply a by 4 into another array:
    c = 4 * a
c will now appear as:
    [
     [0,   4,  8],
     [22, 16, 20],
     [24, 28, 32]
    ]
Now stack horizontally -
np.hstack(c, c))
[
  [0,  1,  2,  0,   4,   8],
  [3,  4,  5, 12,  16,  20],
  [6,  7,  8, 24,  28,  32],
]
the above hstack can also be done with np.concatenate( (,c), axis=1)

Vertical Stacking
=================
Stacking vertically will result in
[
 [ 0,  1,  2],
 [ 3,  4,  5],
 [ 6,  7,  8],
 [ 0,  4,  8],
 [12, 17, 20],
 [24, 28, 32]
]
the above vstack can also be done with np.concatenate( (a,c), axis=0)
Note, the difference between concatenate vertically and horizontally is the value of the axis (0 versus 1)
Note, the axis relates to the position of where the 2nd array (in the above case c), will be positioned.
If vertically, then 0, which results in the 2nd array appearring below.

Depth Stacking
--------------
Depth Stacking flattens each array and pivots it vertically, 
  so [ 
       [0, 1].
       [2, 3]
     ]
would be flattened to 0,1,2,3 and then pivotted:
    0
    1
    2
    3

dstack would stack two arrays (a & c from above), as follows:
    a = [
          [0, 1],
          [2, 3]
        ]
    c = [
          [4, 5],
          [6, 7]
        ]

stacked
[
 [
   [0, 4],
   [1, 5]
 ],
 [
   [2, 6]
   [3, 7]
 ]
]

Column stacking
---------------
Column stacking of one dimensional arrays stacks columns over each other, for example
[0,1,2,3] and [4,5,6,7] would result in
[
 [0, 4],
 [1, 5],
 [2, 6],
 [3, 7]
]

column stacking of 2 dimensional arrays works the same way as hstack

Row stacking
------------
The converse of column_stack is row_stack, which performs row wise stacking for one dimensional arrays, for example:
    [0,1,2,3] and [4,5,6,7] would result in

[
  [0,1,2,3],
  [4,5,6,7]
]
row_stack works like vstack for 2 dimensional arrays.
"""
print(__doc__)
import numpy as np
a = np.arange(9).reshape(3,3)
c = np.copy(a)

c = 4 * a
print(a)
print("\n{}".format(c));
print("Horizontally stacking of above 2 arrays using np.hstack():\n{}".format(np.hstack((a,c))))
print("Note, the same output as hstack can be achieved with np.concatenate((array1, array2), axis=1)")

print("Vertical stacking of above 2 arrays using np.vstack:\n{}".format(np.vstack((a,c))))
print("Note, the same output as vstack can be achieved with np.concatenate((array1, array2)), asix=0)")

print("Depth stacking of the above 2 arrays using np.dstack():\n{}".format(np.dstack((a,c))))
print("Compare row_stack to vstack to prove they result in the same output:\n{}".format(np.row_stack((a,c))==np.vstack((a,c))))
