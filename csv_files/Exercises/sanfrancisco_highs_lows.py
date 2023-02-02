from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

# ! All of 2018, San Francisco, CA
path = Path('../data/san_francisco_2018_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[7])
        low = int(row[8])
    except ValueError:
        print(f'Missing data for {current_date}')
    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)

# Plot the dates and high temperatures
plt.style.use('seaborn-v0_8')
# See available styles with plt.style.available

fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
title = 'Daily high and low temperatures - 2018\nSan Francisco, CA'
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)

ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
