from pathlib import Path
import csv
import matplotlib.pyplot as plt

path = Path('weather_data/Traverse Weather 1980 to 2023.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

#print(header_row)

for index, column_header in enumerate(header_row):
    print(index, column_header)

"""
0 STATION
1 NAME
2 DATE
3 PRCP
4 SNOW
5 SNWD
6 TAVG
7 TMAX
8 TMIN
"""