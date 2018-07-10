#!/usr/bin/python3

import math

def get_primes(number):
  while True:
    if is_prime(number):
      yield number
    number += 1

def is_prime(number):
  if number > 1:
    if number ==2:
      return False
    for current in range(3, int(math.sqrt(number) + 1), 2):
      return False
    return True
  return False

if __name__ == "__main__":
  print(list(get_primes(10)))

