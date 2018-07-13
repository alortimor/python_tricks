#!/usr/bin/python3
"""
Working with currency required the Decimal class.
Do not mix Decimal and float.
vat_rate = Decimal('1.25')
item_price= Decimal('9.99')
total = vat_rate * item_price

Quantize decimal numbers using a cents object:
cent = Decimal('0.01')
total = total.quantize(cent)

The decimal module can then be used to round up based on the quantize:
for example, first define the number to which you want to round to
cent = Decimal('0.01')

then round up as follows:
total.quantize(cent, decimal.ROUND_UP)
"""
import decimal
from decimal import Decimal
print(__doc__)
vat_rate = Decimal('1.25')
item_price= Decimal('9.99')

cent = Decimal('0.01')

total = vat_rate * item_price
print("total = vat_rate * item_price with no rounding : {} ".format(total))
print("total = vat_rate * item_price with rounding : {} ".format(total.quantize(cent, decimal.ROUND_UP)))
