#!/usr/bin/python3

from random import randint
import pygal

class Die():
  def __init__(self, num_sides=6):
    self.num_sides = num_sides

  def roll(self):
    return randint(1, self.num_sides)

die_1 = Die()
die_2 = Die()
results = []

for roll_num in range(1000):
  result = die_1.roll() + die_2.roll()
  results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
  frequency = results.count(value)
  frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Results of rolling 2 six sided die 10000 times."
hist.x_labels = ['1','2','3','5','6']

hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')
