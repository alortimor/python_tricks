#!/usr/bin/python3
import matplotlib
import numpy as np
from matplotlib import pyplot as plt

x_values = list(range(1, 5001))
y_values = [ x**3 for x in x_values]

plt.scatter(x_values, y_values, c=x_values, cmap=plt.cm.Reds, edgecolor='none', s=40)


# Set chart title and x,y labels
plt.title("Cube numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of value", fontsize=14)

# Set size of tick labels
plt.tick_params([0, 2000, 0, 1100000])

plt.show()
plt.savefig('cubes_plot.png')
