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

st.write("## Total number of people in India")

popdf = cities[['state_name','population_total']].copy()
popdf.state_name = popdf.state_name.apply(lambda name: name.title())
with st.expander("View Raw data"):
    st.dataframe(popdf)

n = folium.Map(location=[28.667856,77.44979], zoom_start=4)

choropleth = folium.Choropleth(
    geo_data=geojson,
    key_on='feature.properties.NAME_1',
    data=popdf,
    columns=['state_name','population_total'],
    fill_color='BuPu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Total number of people',
    highlight=True
).add_to(n)

# Add popup for each state
for feature in geojson['features']:
    state_name = feature['properties']['NAME_1']
    state_data = popdf[popdf['state_name'] == state_name]
    if not state_data.empty:
        total_literates = state_data.iloc[0]['population_total']
        popup_content = f"State: {state_name}Total number of literates: {total_literates}"
        popup = folium.Popup(popup_content, parse_html=True)
        folium.GeoJson(feature, popup=popup).add_to(n)

# Display the map
st.subheader("States of India, Total number of population")
stf.folium_static(n)
