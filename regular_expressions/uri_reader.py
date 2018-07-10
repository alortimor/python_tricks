#!/usr/bin/python3

import urllib.request
import re

warnings_uri = 'http://www.nws.noaa.gov/view/national.php?prod=SMW&sid=AKQ'
with urllib.request.urlopen(warnings_uri) as source:
  warnings_text = source.read()

print(warnings_text[:80])

document = warnings_text.decode("UTF-8")
print(document [:80])

title_pattern = re.compile(r"\<h1\>(.*?)\</h1\>")
print(title_pattern)
print(title_pattern.search(document))




