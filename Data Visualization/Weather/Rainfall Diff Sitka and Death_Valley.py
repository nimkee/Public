from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

pathS = Path('weather_data/sitka_weather_2021_full.csv')
linesS = pathS.read_text().splitlines()

readerS = csv.reader(linesS)
header_rowS = next(readerS)

for index, column_header in enumerate(header_rowS):
        print(index, column_header)

pathD = Path('weather_data/death_valley_2021_full.csv')
linesD = pathD.read_text().splitlines()

readerD = csv.reader(linesD)
header_rowD = next(readerD)

for index, column_header in enumerate(header_rowD):
        print(index, column_header)

# Extract high temperatures
dates, rainS, rainD = [], [], []

for row in readerS:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        rain = float(row[5])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        rainS.append(rain)

for row in readerD:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        rain = float(row[5])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        #dates.append(current_date)
        rainD.append(rain)

print(len(dates))
print(len(rainS))
print(len(rainD))

# Plot the high temperatures
plt.style.use('seaborn-v0_8-pastel')
fig, ax = plt.subplots()
ax.plot(dates, rainS, color='red', alpha=.5)
ax.plot(dates, rainD, color='blue', alpha=.5)
ax.fill_between(dates, rainS, rainD, facecolor='orange', alpha=.2)

#Format plot
title = "Daily Rain, 2021\nDeath Valley vs Sitka"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)

fig.autofmt_xdate()
ax.set_ylabel('Temps (F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
