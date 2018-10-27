#!/usr/bin/python3

import abc

class MediaLoader(metaclass=abc.ABCMeta):
  @abc.abstractmethod
  def play(self):
    pass

  @abc.abstractproperty
  def ext(self):
    pass

  @classmethod
  def __subclasshook__(cls, C):
    if cls is MediaLoader:
      attrs = set(dir(C))
      if set(cls.__abstractmethods__) <= attrs:
        return True

    return NotImplemented

def main():
  class Ogg(MediaLoader):
    ext = '.ogg'
    def play(self):
      pass

  o = Ogg()
  if issubclass(Ogg, MediaLoader):
    print ("Is sub class")

  if isinstance(Ogg(), MediaLoader):
    print("Is instance")

if __name__ == "__main__":
  main()

