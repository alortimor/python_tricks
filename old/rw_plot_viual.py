#!/usr/bin/python3

import matplotlib.pyplot as plt
from random_walk_plot2 import RandomWalk


rw = RandomWalk()
rw.fill_walk()
plt.figure(dpi=256,figsize=(10,6))

point_numbers = list(range(rw.num_points))
# plt.plot(rw.x_values, rw.y_values, linewidth=5, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=5)
plt.plot(rw.x_values, rw.y_values, linewidth=5)
#  plt.plot(0, 0, linewidth=5, c='green', edgecolors='none', s=100)
#  plt.plot(rw.x_values[-1], rw.y_values[-1], linewidth=5, c='red', edgecolors='none', s=1)

# plt.axes().get_xaxis().set_visible(False)
# plt.axes().get_yaxis().set_visible(False)
plt.show()

