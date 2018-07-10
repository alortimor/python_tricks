#!/usr/bin/python3
from urllib.request import urlopen

class WebPage:
  def __init__(self, url):
    self.url = url
    self._content = None

  @property
  def content(self):
    if not self._content:
      print("Retrieving New Page...")
      self._content = urlopen(self.url).read()
    return self._content

if __name__ == "__main__":
  import time
  webpage = WebPage("http://ccphillips.net/")
  now = time.time()
  content1 = webpage.content
  t = time.time() - now 
  print ("time to retrieve - {}".format(t))
  now = time.time()
  content2 = webpage.content
  t = time.time() - now 
  print ("second time to retrieve - {}".format(t))

