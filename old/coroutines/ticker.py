#!/usr/bin/python3

import itertools, asyncio, time

# BEFORE asyncio, i.e. prior to Python 3.5
#def ticker():
#  for i in itertools.count():
#    print(i)
#    time.sleep(1)

async def ticker():
  for i in itertools.count():
    print(i)
    await asyncio.sleep(1)

def schedule_coroutine(target, *, loop=None):
  """Schedules target coroutine in the given event loop

  If not given, *loop* defaults to the current thread's event loop

  Returns the scheduled task.
  """

  if asyncio.iscoroutine(target):
    return asyncio.ensure_future(target, loop=loop)
  raise TypeError("target must be a coroutine, not {!r}".format(type(target)))

def run_in_foreground(task, *, loop=None):
  """ Runs event loop in current thread until the given task completes

  Returns the result of the task.
  For more complex conditions, combine with asyncio.wait()
  To include a timeout, combine with asyncio.wait_for()
  """

  if loop is None:
    loop = asyncio.get_event_loop()
  return loop.run_until_complete(asyncio.ensure_future(task, loop=loop))

def call_in_background(target, *, loop=None, executor=None):
  """Schedules and starts target callable as a background task

  If not given, *loop* defaults to the current thread's event loop
  If not given, *executor*" defaults to the loop's default executor

  Returns the scheduled task.
  """

  if loop is None:
    loop = asyncio.get_event_loop()
  if callable(target):
    return loop.run_in_executor(executor, target)
  raise TypeError("target must be a callable, not {!r}".format(type(target)))

if __name__ == "__main__":
  ticker1 = schedule_coroutine(ticker())
  ticker1
  run_in_foreground(asyncio.sleep(5))
  run_in_foreground(asyncio.sleep(3))
  run_in_foreground(asyncio.sleep(0))
