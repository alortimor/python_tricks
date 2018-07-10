#!/usr/bin/python3

class Apartment(Property):
  valid_laundries = ("coin", "ensuite", "none")
  valid_balconies = ("yes", "no", "solarium")

  def __init__(self, balcony='', laundry='', **kwargs):
    super().__init__(**kwargs)
    self.balcony = balcony
    self.laundry = laundry

  def display(self):
    super().display()
    print("APARTMENT DETAILS")
    print("laundry: %s" % self.laundry)
    print("has balcony: %s" % self.balcony)

  def prompt_init():
    parent
