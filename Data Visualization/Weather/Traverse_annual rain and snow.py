from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

# This weather data is fucked. The data is corrupted / missing / worthless

path = Path('weather_data/Traverse Weather 1980 to 2023.csv')
lines = path.read_text().splitlines()

start_date1980 = datetime(1980, 10, 15)
end_date1980 = datetime(1981, 3, 15)

start_date2023 = datetime(2022, 10, 15)
end_date2023 = datetime(2023, 3, 15)

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
dates1980, highs1980, lows1980, rain1980, snow1980 = [], [], [], [], []
dates2023, highs2023, lows2023, rain2023, snow2023 = [], [], [], [], []
dates, snowfall, highs, lows, rainfall = [], [], [], [], []


#Will need to edit some of this code below -- I got this from GPT so need to review it carefully
#Basically I'll nest an if block in the for loop to catch a specific date range
#An elif block should catch the first and then second date range

""""""

for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')

    try:
        rain = int(row[3])
        snow = int(row[4])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        rainfall.append(rain)
        snowfall.append(snow)
        if start_date1980 <= current_date <= end_date1980:
            dates1980.append(current_date)
            rain1980.append(rain)
            snow1980.append(snow)

        elif start_date2023 <= current_date <= end_date2023:
            dates2023.append(current_date)
            rain2023.append(rain)
            snow2023.append(snow)


"""           
    try:
        precip = int(row[3])
    except ValueError:
        print(f"Missing rain data for {current_date}")
    else:
        rain.append(precip)

    try:
        snow = int(row[4])
    except ValueError:
        print(f"Missing snow data for {current_date}")
    else:
        snowfall.append(snow)
"""
"""

        if start_date1980 <= current_date <= end_date1980:
            dates1980.append(current_date)
            lows1980.append(low)
            highs1980.append(high)
           # prcp1980.append(prcp)
           # snow1980.append(snow)

        elif start_date2023 <= current_date <= end_date2023:
            dates2023.append(current_date)
            lows2023.append(low)
            highs2023.append(high)
           # prcp2023.append(prcp)
           # snow2023.append(snow)
"""

"""
    WILL LIKELY NEED TO INCORPORATE THIS BEFORE THE MAIN CODE
    try:
        low = int(row[4])
        high = int(row[3])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        lows.append(low)
        highs.append(high)
"""
print(len(dates))
#print(rain)
#print(len(lows1980))
print(len(rainfall))
print(len(rain1980))
print(len(rain2023))
#print(snowfall)


# Plot the high temperatures
plt.style.use('seaborn-v0_8-pastel')
fig, ax = plt.subplots()
ax.plot(dates, rainfall, color='red', alpha=.5)
ax.plot(dates, snowfall, color='blue', alpha=.5)
#ax.fill_between(dates, highs, lows, facecolor='orange', alpha=.2)

#Format plot
title = "Daily Snow and rain, 1980 and 2023\nTraverse City"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Rain and Snow in ? for TC', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
