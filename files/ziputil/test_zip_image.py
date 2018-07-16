#!/usr/bin/python3

from zip_processor import ZipProcessor
import sys
from PIL import Image

# test with /home/bluefrog/Pictures/screen1.png

class ScapeZip(ZipProcessor):
  def __init__(self, filename):
    super().__init__(filename)

  def process_files(self):
    for filename in self.temp_directory.iterdir():
      im = Image.open(str(filename))
      scaled = im.resize((640, 480))
      scaled.save(str(filename))

if __name__ == "__main__":
  ScapeZip(*sys.argv[1:2]).process_zip()
