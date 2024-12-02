from pathlib import Path
import csv
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# PROBABLY AM BETTER OFF MAKING TWO SEPARATE PLOTS AND COMPARING THEM SIDE BY SIDE
path = Path('weather_data/Traverse Weather 1980 to 2023 Edited Winter.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

start_date1980 = datetime(1980, 10, 15)
end_date1980 = datetime(1981, 3, 15)

start_date2023 = datetime(2022, 10, 15)
end_date2023 = datetime(2023, 3, 15)
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


for index, column_header in enumerate(header_row):
        print(index, column_header)
"""
# Extract high temperatures

dates1980, highs1980, lows1980, prcp1980, snow1980 = [], [], [], [], []
dates2023, highs2023, lows2023, prcp2023, snow2023 = [], [], [], [], []
dates, snowfall, highs, lows, rain = [], [], [], [], []


#Will need to edit some of this code below -- I got this from GPT so need to review it carefully
#Basically I'll nest an if block in the for loop to catch a specific date range
#An elif block should catch the first and then second date range


for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:

        low = int(row[8])
        high = int(row[7])
        #prcp = int(row[3])
        #snow = int(row[4])

    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        #dates.append(current_date)
        lows.append(low)
        highs.append(high)
        #rain.append(prcp)
        #snowfall.append(snow)

        if start_date1980 <= current_date <= end_date1980:
            dates.append(current_date)
            lows1980.append(low)
            highs1980.append(high)
            #prcp1980.append(prcp)
            #snow1980.append(snow)

        if start_date2023 <= current_date <= end_date2023:
            dates.append(current_date)
            lows2023.append(low)
            highs2023.append(high)
            #prcp2023.append(prcp)
            #snow2023.append(snow)



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
#print(dates)
#print(rain)
print(f"Lows data: {len(lows)}")
print(f"Highs data: {len(highs)}")
print(f"Lows1980 data: {len(lows1980)}")
print(f"Lows2023 data: {len(lows2023)}")
print(f"Total dates: {len(dates)}")
#print(highs)
#print(snowfall)
#print(snow2023)

# Plot the high temperatures
plt.style.use('seaborn-v0_8-pastel')
fig, ax = plt.subplots()


ax.plot(dates, lows1980, color='red', alpha=.5)
ax.plot(dates, lows2023, color='blue', alpha=.5)
#ax.fill_between(dates1980, highs, lows, facecolor='orange', alpha=.2)

#Format plot
title = "Daily Low Temps, 1980 to 2023\nTraverse City"
ax.set_title(title, fontsize=20)
#Trying a shortcut for labeling an axis
ax.set_xlabel('', fontsize=16)

#plt.xlabel('Year', fontsize=16)

#Trying something else
#fig.autofmt_xdate()
ax.xaxis.set_major_locator(mdates.MonthLocator())
fmt = mdates.DateFormatter('%b')
ax.xaxis.set_major_formatter(fmt)

ax.set_ylabel('Temperature', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
"""
title = "Comparison of 1980 and 2023 Lows for TC"
labels = {'x': 'Dates'}
fig = px.bar(x=dates1980, y=lows1980, title=title)
fig.add_trace(px.bar(x=dates2023, y=lows2023).data[0])
fig.show()
"""