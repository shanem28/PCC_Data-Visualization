from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

# ! July 2018, Sitka Alaska
# path = Path('data/sitka_weather_07-2018_simple.csv')

# ! All of 2018, Sitka Alaska
path = Path('data/sitka_weather_2018_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, highs = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    highs.append(int(row[5]))
    dates.append(current_date)

# Plot the dates and high temperatures
plt.style.use('seaborn-v0_8')
# See available styles with plt.style.available

fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Format plot
ax.set_title('Daily high temperatures - 2018', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)

ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
