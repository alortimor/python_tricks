#!/usr/bin/python3

# this is an example of a first class function
def some_function(a,b,**kwargs):
    return (a*b)

print(type(some_function))
print(some_function.__code__.co_varnames)

"""
pure functions are simpler and much easier to test
pure functions offer flexibility for optimisation, by allowing change in evaluation order
a pure function must only modify local variables and only real global variables
a lambda function is an example of a pure function
# for example
some_lambda=lambda x: 2**x

"""

some_lambda=lambda x: 2**x
print(some_lambda(4))

