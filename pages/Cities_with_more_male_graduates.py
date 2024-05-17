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

st.write("## Cities with greater male graduates")

male_graduates_above_2lakh = cities[((cities.male_graduates > 200000))]
with st.expander("View Raw data"):
    st.dataframe(male_graduates_above_2lakh)

m_14 = folium.Map(location=[	28.667856,77.449791], tiles='OpenStreetMap', zoom_start=5)
mc14 = MarkerCluster().add_to(m_14)

# Add points to the map
for idx, row in male_graduates_above_2lakh.iterrows():
    Marker([row['lng'], row['lat']], popup=row['name_of_city']).add_to(mc14)

# Display the map
st.subheader("Locating the cities , male graduates  above 2 lakhs ")
stf.folium_static(m_14)