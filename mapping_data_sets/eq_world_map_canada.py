'''Visualizing XML Earthquake Data from Canada.'''

import xml.etree.ElementTree as ET
import plotly.express as px

all_eq_data = ET.parse('data/canada_eq_30_day.xml')
root = all_eq_data.getroot()
name_space = {'ns': 'http://quakeml.org/xmlns/bed/1.2'}

magnitudes, latitudes, longitudes, eq_titles = [], [], [], []
for quake in root[0].findall('ns:event', name_space):
    magnitudes.append(
        float(quake.find('ns:magnitude/ns:mag/ns:value', name_space).text))
    latitudes.append(quake.find(
        'ns:origin/ns:latitude/ns:value', name_space).text)
    longitudes.append(quake.find(
        'ns:origin/ns:longitude/ns:value', name_space).text)
    eq_titles.append(quake.find('ns:description/ns:text',
                     name_space).text.split(sep='/')[0])

title = 'NEDB Magnitude 1.0+ Earthquakes, Past Month - Generated 2023-02-02'
fig = px.scatter_geo(lat=latitudes, lon=longitudes, size=magnitudes, title=title,
                     color=magnitudes,
                     color_continuous_scale='Viridis',
                     labels={'color': 'Magnitude'},
                     projection='natural earth',
                     hover_name=eq_titles,
                     )
fig.show()
