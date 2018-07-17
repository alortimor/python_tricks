#!/usr/bin/python3
"""
vars() method takes only one parameter and that too is optional.
It takes an object as a parameter which may be can a module, a class, an instance, or any object having __dict__ attribute.

The method returns the __dict__ attribute for a module, class, instance, or any other object if the same has a __dict__ attribute. 
If the object fails to match the __dict__ attribute, it raises a TypeError exception.

What is printed output is based on the following return:
return '{id:3s} : {location:19s} : {max_temp:3d} / {min_temp:3d} /  {precipitation:5.2f}'.format_map(vars(self))


"""

class Summary:
      def __init__(self, id, location, min_temp, max_temp, precipitation):
          self.id = id
          self.location = location
          self.min_temp = min_temp
          self.max_temp = max_temp
          self.precipitation=precipitation

      def __str__(self):
          # using format_map enables building of a dictionary object with the variables
          return '{id:3s} : {location:19s} : {max_temp:3d} / {min_temp:3d} /  {precipitation:5.2f}'.format_map(vars(self))

s = Summary('IAD', 'Dulles Intl Airport', 13, 32, 0.4)
print(__doc__)

print(s)

