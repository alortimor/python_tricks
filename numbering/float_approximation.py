#!/usr/bin/python3
"""
Float often involves an approximation.
Accurate when doing division involving powers of 2.
In other cases discrpencies occur however.
To work with float rounding is required or else the digits beyond
zero may become unweildy, for example:
(19/1555)*(155/19) = 0.9999999999999999

The value 0.9999999999999999 should in fact be 1.
round( (19/155) * (155/19), 3) = 1.0

so 1- ( (19/155) * (155/19) ) will indicate the difference in this case.

Automatic rounding is often performed to hide such errors, but in some rare
cases these inaccuracies are not hidden.

Attempting to convert float to either Decimal or Fraction will result in truncation problems
and some odd looking numbers, for example:
    Fraction(19/25) = Fraction(8832866365939553, 72057594037927936)
    Decimal(19/25) =  Decimal('0.12258064516129031640279123394066118635237216949462890625')


It is important to note that float values are approximations, for example 
8.066e+67
will involve a binary representation.
The actual internal value for 8.066e+67 is:
6737037547376141/2**53*2**226

Note, whem importing multiple modules from a library, you can use () , e.g.
from math import (sin, cos, tan, sqrt, log, frexp)

"""
import fractions
from math import (sin, cos, tan, sqrt, log, frexp)
print(__doc__)

sugar_cups = fractions.Fraction('2.5')
scale_factor = fractions.Fraction(5/8)

print("Using float - float(sugar_cups * scale_factor)): {}".format(float(sugar_cups * scale_factor)))
print("Using float - float(fractions.Fraction('2.5')*fractions.Fraction(5/8)): {}".format(float(fractions.Fraction('2.5') * fractions.Fraction(5/8))))

print("\nOne can mix int and float values or int and decimal or int and fraction. One cannot however mix float with Fraction or Decimal.")
print("\nYou can use math.frexp() to view internal details of a number such as the\n\
mantissa and the exponent, for example math.frexp(8.066E+67) results in {}".format(frexp(8.066E+67)))


