#!/usr/bin/python3
import random

class Animal(object):
  def __init__(self, name):
    self.name = name
    self.can_own_pets = False #most Animals cannot own pets
    self.get_features()

  def give_pet(self, pet):
    if not self.can_own_pets:
      print(self.name+' cannot own a pet!')
    else:
      self.pets.append(pet)

  def is_hungry(self):
    return random.choice([True, False])

  def get_features(self):
    """
    In some classes, get features will be a function
    that uses self.name to extract features.
    In my problem, the features are extracted
    with regular expressions that are determined by
    by the class.
    """
    pass

class Human(Animal):
  def __init__(self, name):
    super(Human, self).__init__(name)
    self.can_own_pets = True
    self.pets = []

class Dog(Animal):
  def __init__(self, name):
    super(Dog, self).__init__(name)

  def bark(self):
    print 'WOOF'

  def get_features(self):
    if 'chihuahua' in self.name:
      self.is_annoying = True
    elif 'corgi' in self.name:
      self.adorable = True
