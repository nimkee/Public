from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime


#   THIS IS WHACK. THE DATA FOR TC CHANGES HALF WAY THROUGH AND NONE OF THE COLUMNS LINE UP

path = Path('weather_data/Traverse Weather 1980.csv')
lines = path.read_text().splitlines()

"""
start_date1980 = datetime(1980, 10, 15)
end_date1980 = datetime(1981, 3, 15)

start_date2023 = datetime(2022, 10, 15)
end_date2023 = datetime(2023, 3, 15)
"""

reader = csv.reader(lines)
header_row = next(reader)

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

for index, column_header in enumerate(header_row):
        print(index, column_header)

# Extract high temperatures
dates, highs, lows = [], [], []

for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        low = int(row[7])
        high = int(row[6])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        lows.append(low)
        highs.append(high)


print(len(dates))

print(len(lows))
print(lows)
print(len(highs))
print(highs)



# Plot the high temperatures
plt.style.use('seaborn-v0_8-pastel')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=.5)
ax.plot(dates, lows, color='blue', alpha=.5)
ax.fill_between(dates, highs, lows, facecolor='orange', alpha=.2)

#Format plot
title = "Daily Temp, 1980\nTraverse City"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temp in F for TC', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
