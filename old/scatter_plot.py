#!/usr/bin/python3
import matplotlib
from matplotlib import pyplot as plt

x_values = [1,2,3,4,5]
y_values = [1, 4, 9, 16, 25]
plt.scatter(x_values, y_values, s=100)


# Set chart title and x,y labels
plt.title("Square numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Suquare of value", fontsize=14)

# Set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()


