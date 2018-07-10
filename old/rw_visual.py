#!/usr/bin/python3

import matplotlib.pyplot as plt
from random_walk_plot import RandomWalk

while True:
  rw = RandomWalk()
  rw.fill_walk()
  plt.figure(dpi=256,figsize=(10,6))

  point_numbers = list(range(rw.num_points))
  plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues ,edgecolor='none', s=5)
  plt.scatter(0, 0, c='green', edgecolors='none', s=10)
  plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=10)
  
  # plt.axes().get_xaxis().set_visible(False)
  # plt.axes().get_yaxis().set_visible(False)
  plt.show()

  continue_plotting = input("Show another random Walk? (y/n) ")
  if continue_plotting == 'n':
    break
