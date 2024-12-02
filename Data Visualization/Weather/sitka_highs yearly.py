from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('weather_data/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
        print(index, column_header)

# Extract high temperatures
dates, highs, lows, rainfall = [], [], [], []

for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    low = int(row[8])
    high = int(row[7])
    rain = float(row[5])
    dates.append(current_date)
    lows.append(low)
    highs.append(high)
    rainfall.append(rain)

print(highs)
print(dates)

# Plot the high temperatures
plt.style.use('seaborn-v0_8-pastel')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=.5)
ax.plot(dates, lows, color='blue', alpha=.5)
ax.fill_between(dates, highs, lows, facecolor='orange', alpha=.2)

#Format plot
ax.set_title("Daily Highs and Lows, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)

fig.autofmt_xdate()
ax.set_ylabel('Temps (F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
