#!/usr/bin/python3

from fractions import Fraction
my_data = ('Rice', Fraction(1/4), 'cups')

one_tuple= ('item')
print(len(one_tuple))

print(my_data[1])


t = ('Kumquat', '2', 'cups')
print("Length of tuple {0}".format(len(t)))
print("How many times does the character 'u' appear in the tuple {0}".format(t.count('u')))

print("Position in the tuple where the word {0} occurs: {1}".format(t[2],t.index(t[2])))

