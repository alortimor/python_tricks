#!/usr/bin/python3
"""
Calculations with fraction values can be done with the fractions module.
Fraction objects can be created from strings, integers, or integer pairs.
Generally you do not create Fraction objects from floating point numbers, as
you might see undesired behaviour.
"""
import fractions

sugar_cups = fractions.Fraction('2.5')
scale_factor = fractions.Fraction(5/8)

f = sugar_cups * scale_factor
print("Fraction for sugar_cups('2.5') * scale_factor(5/8) is: {} ".format(f))

f = fractions.Fraction(24/16);
print("\nIf you supply a fraction that can be simplified\n\
then Python will divide by the common denominator, for example for (24/16),\n\
you can assign it again\n\
simpler_fraction = fractions.Fraction(24/16) , which results in {}".format(f))


