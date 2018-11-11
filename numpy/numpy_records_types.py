#!/usr/bin/python3

"""
Following on from the notes in numpy_data_types.py. one can combine non-scalar types into a 'record'.
A record in numpy is a heterogeneous data type. 

You can create a record definition using dtype, for example:

rec = np.dtype([('first_name', '|S20'), ('last_name', |S50'), ('dob', object)])

You can use the defined record type to create an array of the record type as follows:
ra = np.recarray(10, rec)
ra[0] = ('Tom','Godzilla',datetime(1950,11,30))

You can refer to the data type of an individual field as follows:
print('Data type of first_name field: {}'.format(rec['first_name']))

"""
print(__doc__)
import numpy as np
from datetime import datetime

rec = np.dtype([('first_name', '|S20'), ('last_name', '|S50'), ('dob', object)])
# you can combine the record declaration with an actual definition, but it is best to keep them separate
ra = np.recarray(10, rec)

ra[0] = ('Tom', 'Godzilla',datetime(1950,11,30))
print('Data type of first_name field: {}'.format(rec['first_name']))

print("first name of first record: {} ".format(ra[0].first_name))
