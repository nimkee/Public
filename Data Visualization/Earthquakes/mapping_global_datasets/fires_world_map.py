from pathlib import Path
import json
import plotly.express as px


# Read data as a string and convert to a Python object.
path = Path('eq_data/world_fires_7_day.csv')
contents = path.read_text(encoding='utf-8')
all_fi_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_fi_dicts = all_fi_data['features']

mags, lons, lats, eq_titles = [], [], [], []

for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    eq_titles.append(eq_dict['properties']['title'])

title = all_eq_data['metadata']['title']

#fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title)


fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
        color=mags,
        color_continuous_scale='Viridis',
        labels={'color':'Magnitude'},
        projection='natural earth',
        hover_name=eq_titles,
    )

fig.show()