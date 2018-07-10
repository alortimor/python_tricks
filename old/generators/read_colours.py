#!/usr/bin/python3
import csv, math
from random import random

dataset_filename = 'colors1.csv'

def load_colors(filename):
  with open(filename) as dataset_file:
    lines = csv.reader(dataset_file)
    for line in lines:
      yield tuple(float(y) for y in line[0:3]), line[3]

def generate_colors(count=100):
  for i in range(count):
    yield (random(), random(), random())

def color_distance(color1, color2):
  return math.sqrt(sum((x[0] - x[1]) ** 2 for x in zip(color1, color2)))

def nearest_neighbors(model_colors, num_neighbors):
  model = list(model_colors)
  target = yield
  while True:
    distances = sorted(((color_distance(c[0], target), c) for c in model),)
    target = yield [d[1] for d in distances[0:num_neighbors]]

if __name__ == "__main__":
  model_colors = load_colors(dataset_filename)
  target_colors = generate_colors(3)
  get_neighbours = nearest_neighbors(model_colors, 5)
  next(get_neighbours)

  for color in target_colors:
    print("Target color {} ".format(color))
    distances = get_neighbours.send(color)
    
    for d in distances:
      print(color_distance(color, d[0]), d[1])
