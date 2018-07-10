#!/usr/bin/python3

from collections import Counter

if __name__ == "__main__":
  responses = [
  "vanilla",
  "chocolate",
  "vanilla",
  "vanilla",
  "caramel",
  "strawberry",
  "vanilla",
  "strawberry",
  "caramel",
  "strawberry"
  ]

  print("Responses counter in most votes order {}".format(Counter(responses).most_common()))
  print("Top choice with number of votes {}".format(Counter(responses).most_common(1)[0]))
  print("Top choice without votes {}".format(Counter(responses).most_common(1)[0][0]))
