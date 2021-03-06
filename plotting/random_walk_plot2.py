#!/usr/bin/python3
import matplotlib
from matplotlib import pyplot as plt
from random import choice

def get_step():
  some_direction = choice([1, -1])
  num_distance   = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
  return some_direction * num_distance

class RandomWalk():
  """ A class to generate random walks."""
  def __init__(self, num_points=5000):
    """ Initialise attributes of a walk."""
    self.num_points = num_points
    self.x_values = [0]
    self.y_values = [0]

  def fill_walk(self):
    """ Calculate all the points in the walk."""
    
    # Keep taking steps until the walk reaches the desired length
    while len(self.x_values) < self.num_points:
      # Decide direction to go and how far to go in direction chosen
      x_step = get_step()
      y_step = get_step()

      if x_step == 0 and y_step == 0:
        continue

      # Calculate the next x and y values.
      next_x = self.x_values[-1] + x_step
      next_y = self.y_values[-1] + y_step

      self.x_values.append(next_x)
      self.y_values.append(next_y)
