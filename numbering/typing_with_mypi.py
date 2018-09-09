#!/usr/bin/python3

"""
From Python 3.5 one can use type hints. Refer to https://www.python.org/dev/peps/pep-0484/
Often it is required to assert function parameter types, both input and return types.

"""

from typing import *
from decimal import Decimal
Number = Union[int, float, complex, Decimal]

def temperature(*, f_temp: Optional[Number]=None, c_temp: Optional[Number]=None) -> Dict[str, Number]:
    if c_temp is None:
        return {'f_temp': f_temp, 'c_temp': 5*(f_temp-32)/9}
    if f_temp is None:
        return {'f_temp': 32+9*c_temp/5, 'c_temp': c_temp}
    else:
        raise Exception("Niether Fahrenheit nor Celcius temprature was provided")


print("Temperate in Fahrenheit {} ".format(temperature(c_temp=20))

