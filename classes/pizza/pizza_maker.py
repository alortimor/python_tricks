#!/usr/bin/python3

import pizza as pz
from pizza import make_pizza as mp

# to import all functions from pizza
from pizza import *

pz.make_pizza(12, 'mushrooms','green peppers','extra cheese')

profile= pz.build_profile('peter','koukoulis',age=42,gender='M')

print(profile)

