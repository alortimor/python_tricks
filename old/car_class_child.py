#!/usr/bin/python3

class Car():
  def __init__(self,make,model, year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer = 0
    self.litres_fuel_in_tank = 0

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

  def fill_fuel_tank(self, litres):
    self.litres_fuel_in_tank = litres;

  def show_litres_in_tank(self):
    print("Tank has " + str(self.litres_fuel_in_tank) + " fuel")
    
class Battery():
  def __init__(self, battery_size=70):
    """Initialise the battery's attributes"""
    self.battery_size = battery_size

  def describe_battery(self):
    """Print a statement describing the battery size."""
    print("This car has a " + str(self.battery_size) + "-KWh battery.")

  def get_range(self):
    """Print a statement about the range this battery provides."""
    if (self.battery_size == 70):
      range = 240
    elif (self.battery_size == 85):
      range = 270

    message = "This car can go approximately " + str(range)
    message += " miles on a full charge."
    print(message)

class ElectricCar(Car):
  def __init__(self, make, model, year):
    super().__init__(make, model, year)
    self.battery = Battery()

  def fill_fuel_tank(self):
    print("An electric car does not have a fuel tank")

  def show_litres_in_tank(self):
    self.fill_fuel_tank()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.show_litres_in_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_new_car = Car('audi','a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.fill_fuel_tank(20)
my_new_car.show_litres_in_tank()

my_new_car.odometer = 23
my_new_car.read_odometer()

my_new_car.update_odometer(34)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()

