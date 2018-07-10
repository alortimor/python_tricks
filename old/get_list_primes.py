#!/bin/usr/python3

noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
primes = [x for x in range(2, 8) for x not in noprimes]

print("No prime list: {}".format(noprimes))
print("Prime list: {}".format(primes))
