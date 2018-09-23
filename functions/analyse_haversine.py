#!/home/bluefrog/anaconda3/bin/python3

import haversine_formula as hf
import pathlib
import csv

def analyze():
    source_path = pathlib.Path("waypoints.csv")
    with source_path.open() as source_file:
        reader= csv.DictReader(source_file)
        start = next(reader)
        for point in reader:
            d = hf.nm_haversine(float(start['lat']), float(start['lon']), float(point['lat']), float(point['lon']))
            print(start, point, d)
            start = point

if __name__ == "__main__":
    analyze()

