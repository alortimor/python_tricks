#!/home/bluefrog/anaconda3/bin/python3

"""
Haversine forumla is defined as:
α = sin² ( (lat₂ - lat₁) / 2 ) + cos (lat₁) cos (lat₂) sin² ( (lon₂ - lon₁ ) / 2 )

This results in the central angle: c = 2arc sin (√α)
between 2 points, which is measured in radians.

'lat' refers to Latitude and 'lon' longitude.
Refer to https://en.wikipedia.org/wiki/Haversine_formula for more details.
"""
print(__doc__)
from math import radians , sin, cos, sqrt, asin
from functools import partial

MI = 3959
NM = 3440
KM = 6372


# All parameters up until * can be specified by either position or keyword, whereas
# R however has to be specified by keyword. * is used to separate the 2.
def haversine (lat_1: float, lon_1: float,
               lat_2: float, lon_2: float, *, R: float) -> float:
    delta_lat = radians(lat_2) - radians(lat_1)
    delta_lon = radians(lon_2) - radians(lon_1)
    lat_1 = radians(lat_1)
    lat_2 = radians(lat_2)

    a = sin(delta_lat/2)**2 + cos(lat_1) * cos(lat_2) * sin( delta_lon/2)**2 
    return R * ( 2*asin(sqrt(a)) )

# Using a wrapper function to always calculate in nautical miles, means that
# R can be specified by keyword with the call to the haversine function.
def nm_haversine(*args):
  return haversine(*args, R=NM)

mi_haversine = partial(haversine, R=MI)

# nm_haversine = partial(haversine, R=NM)
print("Haversine (Nautical miles) : {}".format(haversine(10,10,20,20, R=NM)))
print("Haversine (Nautical miles): {}".format(nm_haversine(10,10,20,20)))
print("Haversine (Miles): {}".format(mi_haversine(10,10,20,20)))

print("\nThe benefit of using partial over wrapper functions is:\n\
1. Less code\n\
2. Partials can exist in the middle of more complex code, since there is no need for a 'def'\n\
\n\
However, one consideration is the positioning of *args,\n\
which must be placed first in the parameter list\n\
\n\
An alternative method for defining a function object is to use a lambda, for example:\n\
nm_haversine = lambda *args: haversine(*args, R=NM)")

# nm_haversine redefined
nm_haversine = lambda *args: haversine(*args, R=NM)
print("Haversine (Nautical miles): {} ".format(nm_haversine(10,10,20,20)))
