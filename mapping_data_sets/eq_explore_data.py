'''
Loading JSON data. 
From Chaper 16 of Python Crash Course 2nd Edition by Eric Matthes
'''

import json
from pathlib import Path

# Explore the structure of the data
path = Path('data/eq_data_1_day_m1.geojson')
contents = path.read_text(encoding='UTF-8')
all_eq_data = json.loads(contents)

# # Create a more readable version of the data
# path = Path('data/readable_eq_data.geojson')
# readable_contents = json.dumps(all_eq_data, indent=4)
# path.write_text(readable_contents)

all_eq_dicts = all_eq_data['features']
magnitudes, longitudes, latitudes = [], [], []
for earthquake in all_eq_dicts:
    magnitude = earthquake['properties']['mag']
    longitude = earthquake['geometry']['coordinates'][0]
    latitude = earthquake['geometry']['coordinates'][1]

    magnitudes.append(magnitude)
    longitudes.append(longitude)
    latitudes.append(latitude)

print(magnitudes[:10])
print(latitudes[:10])
print(longitudes[:10])
