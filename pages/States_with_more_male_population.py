import streamlit as st
import streamlit_folium as stf
import pandas as pd
import folium
import geopandas as gpd
import folium
from folium import Choropleth, Circle, Marker
from folium.plugins import HeatMap, MarkerCluster

import json

# Read the CSV file
@st.cache_data
def load_data():
    cities = pd.read_csv("data/cities.csv")
    cities['lng'] = [float(i.split(',')[0]) for i in cities.location]
    cities['lat'] = [float(i.split(',')[1]) for i in cities.location]
    ind_states = "data/india_state_geo.json"
    with open(ind_states) as f:
        geojson = json.load(f)
    return geojson, cities

st.title("Population of Cities in India")
geojson, cities = load_data()

st.write("## States with more male population in India")

popm = cities[['state_name','population_male']].copy()
popm.state_name = popm.state_name.apply(lambda name: name.title())
with st.expander("View Raw data"):
    st.dataframe(popm)

n5 = folium.Map(location=[28.667856, 77.44979], zoom_start=4)

choropleth = folium.Choropleth(
    geo_data=geojson,
    data=popm,
    columns=popm.columns.tolist(),
    key_on='feature.properties.NAME_1',
    fill_color="RdPu",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Male Population",
    highlight=True,
).add_to(n5)

# Add popup for each state
for feature in geojson['features']:
    state_name = feature['properties']['NAME_1']
    state_data = popm[popm['state_name'] == state_name]
    if not state_data.empty:
        male_population = state_data.iloc[0]['population_male']
        popup_content = f"State: {state_name}Male Population: {male_population}"
        popup = folium.Popup(popup_content, parse_html=True)
        folium.GeoJson(feature, popup=popup).add_to(n5)

# Display the map
st.subheader("States of India, States with more male population")
stf.folium_static(n5)
