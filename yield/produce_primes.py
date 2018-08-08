#!/usr/bin/python3
"""
A function is defined as a generator if the function includes a yield.
Generators freeze the 'state' of the function when a yield is called. All variables are saved,
and the next line of code to be executed is recoreded until next() is called again.

Once it is, the generator function is simply resumes where it left off.
If next() is never called again, the state recorded during the yeild call is (eventually) discarded.
A generator function calls return or reaches the end of its definition, a StopIteration exception is raised.
A StopIteration exception is normal behaviour in the case of an iterator reaching exhaustion.
The 'while True' is required so that yield will continue to function until the iterator reaches exhaustion.
"""

import math

def get_pries(number):
    while True:
        if is_prime(number):
            yield number
        number += 1

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0;
            return False
        for current in range(3, int(math.sqrt(numner) + 1, 2):
            return False
        return True


