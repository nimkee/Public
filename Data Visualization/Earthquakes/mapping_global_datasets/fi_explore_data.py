from pathlib import Path
import csv
import plotly.express as px


# Read data as a string and convert to a Python object.
path = Path('eq_data/world_fires_7_day.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

"""
Column Headers:
0 latitude
1 longitude
2 brightness
3 scan
4 track
5 acq_date
6 acq_time
7 satellite
8 confidence
9 version
10 bright_t31
11 frp
12 daynight
"""

lons, lats, brights = [], [], []

for row in reader:
    lons.append(row[1])
    lats.append(row[0])
    brights.append(float(row[2]))

print(lons)
print(lats)
print(brights)

title = 'Global (Forest?) Fires'
fig = px.scatter_geo(lat=lats, lon=lons, size=brights, title=title,
                     color=brights,
                     color_continuous_scale='inferno',
                     labels={'color':'Brightness'},
                     projection='natural earth',
                     )

fig.show()