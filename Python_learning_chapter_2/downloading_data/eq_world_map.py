import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of this data.
filename ='Python_learning_chapter_2/downloading_data/data/eq_data_30_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dict = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dict:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker':{
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Earth',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]

my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')