#!/usr/bin/python3

import re

def match_re(filename, regex):
  with open(filename) as file:
    lines = file.readlines()
  for line in reversed(lines):
    match = re.match(regex, line)
    if match:
      regex = yield match.groups()[0]

def extract_hex(filename):
  DATE_RE = '^\d\d/\\d\d/\\d\d\d\d$'
  matcher = match_re(filename, DATE_RE)
  extract = next(matcher)
  while True:
    signal = matcher.send('^\d\d:\d\d SIGNAL \((0x..)*\)$'.format(re.escape(extract)))
    hex_value = matcher.send('{} \(SERIAL=([^)]*)\)'.format(signal))
    yield hex_value
    extract = matcher.send(DATE_RE)

if __name__ == "__main__":
  for hex_value in extract_hex('sample_kern_log.log'):
    print(hex_value)

