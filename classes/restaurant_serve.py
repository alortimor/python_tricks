#!/usr/bin/python3

class Restaurant():
  """ A simple class for a dog """
  def __init__(self, restaurant_name, cuisine_type): 
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type 
    self.number_served = 0

  def open_restaurant(self):
    print(self.restaurant_name.title() + " is open!")

  def describe_restaurant(self):
    print("Restaurant name is " + self.restaurant_name.title()) 
    self.open_restaurant()

  def update_number_served(self, customers_served):
    self.number_served = customers_served

  def show_how_many_served(self):
    print("Number of customers served: " + str(self.number_served))

greek_restaurant = Restaurant('Zorba the Greek', 'greek')
thai_restaurant = Restaurant('Bangkok Special', 'Thai')
italian_restaurant = Restaurant('Roma', 'Italian')
greek_restaurant.describe_restaurant()
thai_restaurant.describe_restaurant()
italian_restaurant.describe_restaurant()

thai_restaurant.number_served = 10
thai_restaurant.show_how_many_served()

thai_restaurant.update_number_served(20)
thai_restaurant.show_how_many_served()

