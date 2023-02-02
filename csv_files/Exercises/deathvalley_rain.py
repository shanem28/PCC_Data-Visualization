from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

# ! All of 2018, Death Valley CA
path = Path('../data/death_valley_2018_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, rainfall = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    rainfall.append(float(row[3]))
    dates.append(current_date)

# Plot the dates and precipitation
plt.style.use('seaborn-v0_8')
# See available styles with plt.style.available

fig, ax = plt.subplots()
ax.plot(dates, rainfall, c='red')

# Format plot
ax.set_title('Daily Precipitation - 2018\n Death Valley, CA', fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Rainfall (in)', fontsize=16)

ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
