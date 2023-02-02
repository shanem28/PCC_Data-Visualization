'''
Visualization of earthquake data using Plotly. 
From Chaper 16 of Python Crash Course 2nd Edition by Eric Matthes
'''

import json
from pathlib import Path
import plotly.express as px
from datetime import datetime


def load_JSON(path: Path, magnitudes: list, longitudes: list, latitudes: list, eq_titles: list):
    ''' Function to load JSON data in from a specified Path.

    Arguments:
        path -- Path link to load data
        magnitudes -- Empty list to store EQ Magnitudes
        longitudes -- Empty list to store Longitudes
        latitudes -- Empty list to store Latitudes
        eq_titles -- Empty list to store descriptions of EQ
    '''
    global chart_title
    contents = path.read_text(encoding='UTF-8')
    all_eq_data = json.loads(contents)

    all_eq_dicts = all_eq_data['features']

    for earthquake in all_eq_dicts:
        magnitudes.append(earthquake['properties']['mag'])
        longitudes.append(earthquake['geometry']['coordinates'][0])
        latitudes.append(earthquake['geometry']['coordinates'][1])
        eq_titles.append(earthquake['properties']['title'])

    gen_date = datetime.fromtimestamp(
        all_eq_data['metadata']['generated']/1000)
    gen_date = gen_date.strftime("%Y-%m-%d")

    chart_title = all_eq_data['metadata']['title']+' - Generated ' + gen_date


def plot_data(latitudes: list, longitudes: list, magnitudes: list):
    '''Plot data on a scatter geo plot'''
    fig = px.scatter_geo(lat=latitudes, lon=longitudes, size=magnitudes, title=chart_title,
                         color=magnitudes,
                         color_continuous_scale='Viridis',
                         labels={'color': 'Magnitude'},
                         projection='natural earth',
                         hover_name=eq_titles,
                         )
    fig.show()


if __name__ == "__main__":
    path = Path('data/eq_data_30_day_m1.geojson')
    magnitudes, longitudes, latitudes, eq_titles = [], [], [], []
    load_JSON(path, magnitudes, longitudes, latitudes, eq_titles)
    plot_data(latitudes, longitudes, magnitudes)
