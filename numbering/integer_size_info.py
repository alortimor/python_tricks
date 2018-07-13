#!/usr/bin/python3
import sys
import math

print("sys.maxsize shows the largest of the small integers ".format(sys.maxsize)) 
print("Max size of integers can be obtained using math.log(sys.maxsize,2) : {} ".format(math.log(sys.maxsize,2)))
print("Therefore the range is -2^64 ... 2^63 - 1")
print("sys.int_info shows the maximum of the small integer values {} ".format(sys.int_info)) 
print("Common small numbers, -5 to 256, are stored in a pool of objects to optimize memory.\n\
You can use id(1) to view the object id of 1: {}".format(id(1)))

print("\nUse len(str()) to find out the number of digits of a number, for example for 2**2048, the length is: {} ".format(len(str(2**2048)))) 

print ("\n+ - addition")
print ("- - subtraction")
print ("* - multiplication")
print ("/ - true division")
print ("// - floor division")
print("& - bit wise AND")
print("^ - bit wise exclusive OR")
print("| - bit wise Inclusive OR")
print("<< - bit wise LEFT SHIFT")
print(">> - bit wise RIGHT SHIFT")

xor = 0b0011 ^ 0b0111
composite_byte = 0b01101100
shifted_result = bin(composite_byte >> 6)
print ("\nExample of exlusive OR with: xor = 0b0011 ^ 0b0111: {} ".format(bin(xor)))
print ("\nExample of a bitwise RIGHT SHIFT, based on\n\
composite_byte = 0b01101100\n\
shifted_result = bin(composite_byte >> 6): {} ".format(shifted_result))


bottom_6_mask = 0b0111111
and_result = bin(composite_byte & bottom_6_mask)
print ("\nExample of a bitwise AND, based on\n\
bottom_6_mask = 0b0111111\n\
and_result = bin(composite_byte & bottom_6_mask): {} ".format(and_result))
