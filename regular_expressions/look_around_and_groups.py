import re

text="INFO 2018-07-05 22:05:00,487 authentication failed"


pattern = re.compile(r'\w+\s[\d-]+\s[\d:,]+\s(.*\sfailed)')

match = pattern.match(text)
if match:
  print("The following text' + text + ' is matched  )
