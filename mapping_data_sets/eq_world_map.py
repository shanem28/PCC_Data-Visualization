import json
from pathlib import Path
import plotly.express as px
from datetime import datetime

# Explore the structure of the data
path = Path('data/eq_data_30_day_m2.5.json')
contents = path.read_text(encoding='UTF-8')
all_eq_data = json.loads(contents)

all_eq_dicts = all_eq_data['features']

magnitudes, longitudes, latitudes, eq_titles = [], [], [], []
for earthquake in all_eq_dicts:
    magnitudes.append(earthquake['properties']['mag'])
    longitudes.append(earthquake['geometry']['coordinates'][0])
    latitudes.append(earthquake['geometry']['coordinates'][1])
    eq_titles.append(earthquake['properties']['title'])

gen_date = datetime.fromtimestamp(all_eq_data['metadata']['generated']/1000)
gen_date = gen_date.strftime("%Y-%m-%d")

title = all_eq_data['metadata']['title']
title += ' - Generated ' + gen_date
fig = px.scatter_geo(lat=latitudes, lon=longitudes, size=magnitudes, title=title,
                     color=magnitudes,
                     color_continuous_scale='Viridis',
                     labels={'color': 'Magnitude'},
                     projection='natural earth',
                     hover_name=eq_titles,
                     )
fig.show()
