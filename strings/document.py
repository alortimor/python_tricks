#!/usr/bin/python3

from cursor import Cursor
from character import Character

class Document:
  def __init__(self):
    self.characters = []
    self.cursor = Cursor(self)
    self.filename = ''

  def insert(self, character):
    if not hasattr(character, 'character'):
      character = Character(character)
    self.characters.insert(self.cursor.position, character)
    self.cursor.forward()

  def delete(self):
    del self.characters[self.cursor.position]

  def save(self):
    with open(self.filename, 'w') as f:
      f.write(''.join((str(c) for c in self.characters)))
    f.close()

  @property
  def string(self):
    return "".join((str(c) for c in self.characters))

if __name__ == "__main__":
  doc = Document()
  doc.filename = "test_doc.txt"
  doc.insert(Character('H', bold=True))
  doc.insert('e')
  doc.insert('l')
  doc.insert('l')
  doc.insert('o')
  doc.insert('\n')
  doc.insert(Character('W', bold=True))
  doc.insert('o')
  doc.insert('r')
  doc.insert('l')
  doc.insert('d')
  doc.insert('\n')
  doc.cursor.home()
  doc.delete()
  doc.insert(Character('W', italic=True))
  print(doc.string)
  doc.save()

