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
geojson,data = load_data()

st.write("## Population Study")

state = st.selectbox("Select a state to filter data", data.state_name)
state_data = data[data['state_name'] == state]
# st.warning(state_data.shape)
# Create a Folium map
st.write("## Map of Population Distribution in States")
# st.map(state_data)
m_1 = folium.Map(location=[	22,77], tiles='cartodbpositron', zoom_start=5)
mc1 = MarkerCluster().add_to(m_1)
# Add points to the map
for idx, row in state_data.iterrows():
    Marker([row['lng'], row['lat']],
           popup=f'{row["name_of_city"]} {row["population_total"]}').add_to(mc1)

# Display the map
stf.folium_static(m_1)
