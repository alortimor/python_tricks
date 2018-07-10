#!/usr/bin/python3

import sys

# replace the " WARNING" column with nothing in sample_log.dat
def warnings_filter(insequence):
  for l in insequence:
    if 'WARNING' in l:
      ll = l
      yield l.replace(' WARNING','')

if __name__ == "__main__":
  inname, outname = sys.argv[1:]
  with open(inname) as infile:
    with open(outname, "w") as outfile:
      filter = warnings_filter(infile)
      for l in filter:
        outfile.write(l)

