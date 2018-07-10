#!/usr/bin/python3

from timed_event import Timer
import datetime

def format_time(message, *args):
  now = datetime.datetime.now().strftime("%I:%M:%S")
  print(message.format(*args, now=now))

def one(timer):
  format_time("{now}: Called One")


def two(timer):
  format_time("{now}: Called Two")

def three(timer):
  format_time("{now}: Called Three")

class Repeater:
  def __init__(self):
    self.count = 0

  def repeater(self, timer):
    format_time("{now}: repeat {0}", self.count)
    self.count += 1
    timer.call_after(5, self.repeater)


if __name__ == "__main__":
  timer = Timer()
  timer.call_after(1, one)
  timer.call_after(2, one)
  timer.call_after(2, two)
  timer.call_after(4, two)
  timer.call_after(3, three)
  timer.call_after(6, three)
  repeater = Repeater()
  timer.call_after(5, repeater.repeater)
  format_time("{now}: Starting")
  for e in timer.events:
    print("{} Called after {} ".format(e.callback.__name__, e.endtime.strftime("%I:%M:%S")))
  #timer.run()

