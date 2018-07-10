#!/usr/bin/python3

class Character:
  def __init__(self, character, bold=False, underline=False, italic=False):
    assert len(character) == 1
    self.character = character
    self.bold = bold
    self.underline = underline
    self.italic = italic

  def __str__(self):
    bold = "*" if self.bold else ''
    italic = "/" if self.italic else ''
    underline = "_" if self.underline else ''
    return bold + italic + underline + self.character
