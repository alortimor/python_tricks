#!/usr/bin/python3

import datetime
import time

class TimedEvent:
  def __init__(self, endtime, callback):
    self.endtime = endtime
    self.callback = callback

  def ready(self):
    return self.endtime <= datetime.datetime.now()

class Timer:
  def __init__(self):
    self.events = []

  def call_after(self, delay, callback):
    end_time = datetime.datetime.now() + datetime.timedelta(seconds=delay)

    self.events.append(TimedEvent(end_time, callback))

  def run(self):
    while True:
      ready_events = (e for e in self.events if e.ready())
      for event in ready_events:
        event.callback(self)
        self.events.remove(event)
      time.sleep(0.5)

if __name__ == "__main__":
  def format_time(message, *args):
    now = datetime.datetime.now().strftime("%I:%M:%S")
    print(message.format(*args, now=now))

  def one(timer):
    format_time("{now}: Called One")

  timer = Timer()
  timer.call_after(1, one)
  timer.call_after(2, one)
  for e in timer.events:
    print("{} Called after {} ".format(e.callback.__name__(), e.endtime.strftime("%I:%M:%S")))
  #timer.run()

