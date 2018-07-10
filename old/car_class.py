#!/usr/bin/python3

class Car():
  def __init__(self,make,model, year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer = 0

  def get_descriptive_name(self):
    long_name = str(self.year) + ' ' + self.make + ' ' + self.model
    return long_name.title()

  def read_odometer(self):
    print("This car has " + str(self.odometer) + " kilometres clocked")

  def update_odometer(self, kilometres):
    if (kilometres > self.odometer):
      self.odometer = kilometres
    else:
      print("You cannot roll back a vehicle's odometer")

  def increment_odometer(self, kilometres):
      self.odometer += kilometres

my_new_car = Car('audi','a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer = 23
my_new_car.read_odometer()

my_new_car.update_odometer(44)
my_new_car.read_odometer()

my_new_car.update_odometer(34)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()

