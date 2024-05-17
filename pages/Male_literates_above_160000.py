import streamlit as st
import streamlit_folium as stf
import pandas as pd
import folium
import geopandas as gpd
import folium
from folium import Choropleth, Circle, Marker
from folium.plugins import HeatMap, MarkerCluster

# Read the CSV file
@st.cache_data
def load_data():
    cities=pd.read_csv(r"data/cities.csv")
    cities['lng'] = [float(i.split(',')[0]) for i in cities.location ]
    cities['lat'] = [float(i.split(',')[1]) for i in cities.location ]
    ind_states =r"india_state_geo.json"
    return ind_states, cities

st.title("Population of Cities in India")
geojson,cities = load_data()

st.write("## Male Literacy Study")

Male_literates_above_160000 = cities[((cities.literates_male > 160000))]
with st.expander("View Raw data"):
    st.dataframe(Male_literates_above_160000)
m_5 = folium.Map(location=[	28.667856,77.449791], tiles='OpenStreetMap', zoom_start=5)
mc5 = MarkerCluster().add_to(m_5)

# Add points to the map
for idx, row in Male_literates_above_160000.iterrows():
    Marker([row['lng'], row['lat']], popup=row['name_of_city']).add_to(mc5)

# Display the map
st.subheader(" Locating Male literates above 160000 ")
stf.folium_static(m_5)