#!/home/bluefrog/anaconda3/bin/python3
"""

The following is an incorrect definition of the function conver_temperature:

def convert_temperature(*, f_temp: Optional[Number]=None, c_temp: Optional[Number]=None) -> Number:
  if c_temp is None:
    c_temp = 5*(f_temp-32)/9
  elif f_temp is None:
    f_temp = 32+9*c_temp/5
  else:
  raise Exception( "Logic Design Problem" )
    result = {'c_temp': c_temp,
              'f_temp': f_temp} # type: Dict[str, Number]
  return result

It is incorrect due to the actual return being a dictionary, whereas the type hint specifies a "Number"

"""

from decimal import Decimal
from typing import Optional, Union, Dict
Number = Union[int, float, Decimal]

def convert_temperature(*, f_temp: Optional[Number]=None, c_temp: Optional[Number]=None) -> Number:
  if c_temp is None:
    c_temp = 5*(f_temp-32)/9
  elif f_temp is None:
    f_temp = 32+9*c_temp/5
  else:
    raise Exception( "Logic Design Problem" )
    result: Dict[str, Number] = {'c_temp': c_temp,
                                 'f_temp': f_temp}
  return result



