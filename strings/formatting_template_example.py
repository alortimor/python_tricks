#!/usr/bin/python3
"""
Complex strings can be created using placeholders {} within a quoted string".
The placeholders are substituted by the variables passed to a format function.
Such a complex string is referred to as a template.
Templates with substitution allow for rules to put data into a more complex format.
Detailed description of format rules are avaialble at : https://docs.python.org/3/library/string.html#string-formatting

vars() method takes only a single (optional) parameter.
It takes an object as a parameter which can be either a module, class, an instance, or any object having __dict__ attribute.

The method returns the __dict__ attribute for a module, class, instance, or any other object, providing it has a __dict__ attribute. 
If the object fails to match the __dict__ attribute, it raises a TypeError exception.

The  code example below prints output based on the following template:
return '{id:3s} : {location:19s} : {max_temp:3d} / {min_temp:3d} /  {precipitation:5.2f}'.format_map(vars(self))

The format rules used in the above example are:
    3s = string of 3 characters
    19s = string of 19 characters
    3d = three digits

Other rules for templates include:
    b = binary
    c = Unicode
    x = hexadecimal
    o = octal
    % = represent the number as a percentage
    f = floating point
    e = for scientific notations. For example 6.626E-34 or 6.626e-34
    g = Switches automatically between e and f to keep the output in the given sized field. 
        For exampe, for a format of 20.5G , up to 20-digit numbers will be displayed using f formatting. 
        Larger numbers will use e formatting.

    > = right align
    < = left alighn
    ^ = centre
    
    + = show numbers with a sign regardless of whether they are positive or negative
    - = only show numbers that are negative with a - sign

     Digits and strigs only need a width, floating-point values  however require a width and precision, specified as width.precision.
"""

class Summary:
      def __init__(self, id, location, min_temp, max_temp, precipitation):
          self.id = id
          self.location = location
          self.min_temp = min_temp
          self.max_temp = max_temp
          self.precipitation=precipitation

      def __str__(self):
          return '{id:3s} : {location:19s} : {max_temp:3d} / {min_temp:>3d} /  {precipitation:>5.2f}'.format_map(vars(self))
          # return '{id:3s} : {location:19s} : {max_temp:3d} / {min_temp:<3d} /  {precipitation:<5.2f}'.format_map(vars(self))

s = Summary('IAD', 'Dulles Intl Airport', 13, 32, 0.4)
print(__doc__)

print(s)

