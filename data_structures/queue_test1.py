#!/usr/bin/python3

from queue import Queue, LifoQueue, PriorityQueue

if __name__ == "__main__":

  # Queue
  lineup = Queue(maxsize=3)

  # the next line will raise an error if called without any entries on the queue
  # lineup.get(block=False)

  lineup.put("one")
  lineup.put("two")
  lineup.put("three")

  # the following 2 lines will raise errors, since q size can only accommodate a maximum of 3 entries
  # lineup.put("four", timeout=1)
  # lineup.put("five", timeout=1)

  print(lineup.full())
  print(lineup.get())
  print(lineup.get())
  print(lineup.full())
  print(lineup.get())
  print(lineup.empty())

  # LifoQueue
  stack = LifoQueue(maxsize=3)
  stack.put("one")
  stack.put("two")
  stack.put("three")
  # the following line will raise an error, size q sze can only accommodate a maximum of 3 entries
  # stack.put("four", block=False)
  print(stack.full())
  print(stack.get())
  print(stack.get())
  print(stack.get())
  print(stack.empty())

  # PriorityQueue
  heap = PriorityQueue(maxsize=4)
  heap.put((3, "three"))
  heap.put((2, "two"))
  heap.put((4, "four"))
  heap.put((1, "one"))
  while not heap.empty():
    print(heap.get())

    
  
  
