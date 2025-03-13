import csv
from pathlib import Path 
from matplotlib import pyplot as plt
from datetime import datetime

path = Path("death_valley_2021_simple.csv")
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header = next(reader)
dates, highs, lows = [], [], []
fig, ax = plt.subplots()

for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        single_high = int(row[3])
        single_low = int(row[4])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(single_high)
        lows.append(single_low)

ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)

ax.set_title("Daily High and Low Temperatures, July 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.show()
