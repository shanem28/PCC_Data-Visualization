from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime


def getWeatherData(path, dates, highs, lows, location):
    '''Attempt to open a CSV file with specified filename and load in weather
    data to globally defined lists. Data Index found automatically based on name.

    Arguments:
        path -- Path to weather data\n
        dates -- An empty list for storing date data\n
        highs -- An empty list for storing high temp data\n
        lows -- An empty list for storing low temp data\n
    '''
    lines = path.read_text().splitlines()

    reader = csv.reader(lines)
    header_row = next(reader)

    name_index = header_row.index('NAME')
    date_index = header_row.index('DATE')
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')

    for row in reader:
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = int(row[high_index])
            low = int(row[low_index])
        except ValueError:
            print(f'Missing data for {current_date}')
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)
            location.append(row[name_index])


def plotData(ax, dates: list, highs: list, lows: list, *, alpha_v: float):
    '''Plot the high and low weather data to a pyplot subplot.

    Arguments:
        ax -- Pyplot Axes object for suplot\n
        dates -- list of dates of data\n
        highs -- list of high temperatures\n
        lows -- list of low temperatures\n
        alpha_v -- keyword argument for alpha vaule of plot\n
    '''
    ax.plot(dates, highs, c='red', alpha=alpha_v)
    ax.plot(dates, lows, c='blue', alpha=alpha_v)
    ax.fill_between(dates, highs, lows, facecolor='blue', alpha=(alpha_v/6))


plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

title = 'Daily high and low temperatures - 2018'

# Load in and plot Sitka, AK Weather data
path = Path('../data/sitka_weather_2018_simple.csv')
dates, highs, lows, location = [], [], [], []
getWeatherData(path, dates, highs, lows, location)
plotData(ax, dates, highs, lows, alpha_v=0.6)
title += '\n' + location[0]

# Load in and plot Death Valley, CA weather data
path = Path('../data/death_valley_2018_simple.csv')
dates, highs, lows, location = [], [], [], []
getWeatherData(path, dates, highs, lows, location)
plotData(ax, dates, highs, lows, alpha_v=0.3)
title += ' and ' + location[0]

# Format plot
ax.set_title(title, fontsize=18)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)

ax.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(10, 130)

plt.show()
