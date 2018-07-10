#!/usr/bin/python3

import gzip, socket
from io import BytesIO

class GzipSocket:
  def __init__(self, socket):
    self.socket = socket

  def send(self, data):
    buf = BytesIO()
    zipfile = gzip.GzipFile(fileobj=buf, mode='w')
    zipfile.write(data)
    zipfile.close()
    self.socket.send(buf.getvalue())

  def close(self):
    self.socket.close()


class LogSocket:
  def __init__(self, socket):
      self.socket = socket

  def send(self, data):
      print( "Sending {0} to {1}".format(data, self.socket.getpeername()[0]) )
      self.socket.send(data)

  def close(self):
      self.socket.close()

def respond(client, response):
  client.send(bytes(response, 'utf8'))
  client.close()

if __name__ == "__main__":

  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind(('localhost',2401))
  server.listen(1)

  try:
    while True:
      response = input("Enter a value: ")
      gzip_yes = input("Gzip data prior to sending (Y/N) : ")
      client, addr = server.accept()
      if gzip_yes in ('N','n'):
        client = LogSocket(client)
      else:
        client = GzipSocket(client)
      respond(client, response)
  finally:
    server.close()
