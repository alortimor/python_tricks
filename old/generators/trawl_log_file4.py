#!/usr/bin/python3

import sys

# replace the " WARNING" column with nothing in sample_log.dat
def warnings_filter(infilename):
  with open(infilename) as infile:
    yield from (l.replace(' WARNING','') for l in infile if 'WARNING' in l)

if __name__ == "__main__":
  inname, outname = sys.argv[1:]
  filter = warnings_filter(inname)
  with open(outname, "w") as outfile:
    for l in filter:
      outfile.write(l)

