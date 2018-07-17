#!/usr/bin/python3
import matplotlib
from matplotlib import pyplot as plt

x_values = list(range(1, 1001))
y_values = [ x**2 for x in x_values]

plt.scatter(x_values, y_values, c=x_values, cmap=plt.cm.Blues, edgecolor='none', s=40)


# Set chart title and x,y labels
plt.title("Square numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Suquare of value", fontsize=14)

# Set size of tick labels
plt.tick_params([0, 1100, 0, 1100000])

plt.show()
plt.savefig('squares_plot.png')
