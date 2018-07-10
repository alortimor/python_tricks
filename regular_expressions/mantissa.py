#!/usr/bin/python3

import math
example_value = (63/25) * (17 + 15* math.sqrt(5)) / (7 + 15 * math.sqrt(5))
mantissa_fraction, exponent = math.frexp(example_value)
mantissa_whole = int(mantissa_fraction*2**53)
message_text = ('The internal representation'
              ' is {mantissa:d}/2**53*2**{exponent:d}').format(mantissa=mantissa_whole
                                                              ,exponent=exponent)
print(message_text)

