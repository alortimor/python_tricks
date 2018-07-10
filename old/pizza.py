#!/usr/bin/python3


def make_pizza(size, *toppings):
  print ("\nMaking a " + str(size) + "-cm pizza with the following toppings:")

  for topping in toppings:
    print ("- " + topping)

def build_profile(first, last, **user_info):
  """Build a dictionary containing everything known about a user"""
  profile={}
  profile['first_name'] = first
  profile['last_name']  = last
  for key, value in user_info.items():
    profile[key] = value

  return profile


