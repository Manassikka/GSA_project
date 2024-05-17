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

st.write("## States with more Literate Males in India")

popelrm = cities[['state_name','effective_literacy_rate_male']].copy()
popelrm.state_name = popelrm.state_name.apply(lambda name: name.title())
with st.expander("View Raw data"):
    st.dataframe(popelrm)

n7 = folium.Map(location=[28.667856, 77.44979], zoom_start=4)

choropleth = folium.Choropleth(
    geo_data=geojson,
    data=popelrm,
    columns=popelrm.columns.tolist(),
    key_on='feature.properties.NAME_1',
    fill_color="PuBu",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Effective Literacy Rate of Males",
    highlight=True,
).add_to(n7)

# Add popup for each state
for feature in geojson['features']:
    state_name = feature['properties']['NAME_1']
    state_data = popelrm[popelrm['state_name'] == state_name]
    if not state_data.empty:
        literacy_rate = state_data.iloc[0]['effective_literacy_rate_male']
        popup_content = f"State: {state_name}Effective Literacy Rate of Males: {literacy_rate}%"
        popup = folium.Popup(popup_content, parse_html=True)
        folium.GeoJson(feature, popup=popup).add_to(n7)

# Display the map
st.subheader("States of India,with more Literate Males")
stf.folium_static(n7)
