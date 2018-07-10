#!/usr/bin/python3

import unittest
from format_name import get_formatted_name

class NamesTestCase(unittest.TestCase):
  """Tests for 'format_name.py' """

  def test_first_last_name(self):
    """Do names like 'Janis Joplin' work? """
    formatted_name = get_formatted_name('janis', 'joplin')
    self.assertEqual(formatted_name, 'Janis Joplin')

  def test_first_last_middle_name(self):
    """Do names like 'Janis Joplin' work? """
    formatted_name = get_formatted_name('Peter', 'Koukoulis', 'Michael')
    self.assertEqual(formatted_name, 'Peter Michael Koukoulis')

unittest.main()
