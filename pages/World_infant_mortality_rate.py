import streamlit as st
import plotly.express as px
import pandas as pd

# Load data from CSV file
countries = pd.read_csv(r"C:\Users\manas\OneDrive\Documents\GSA_project\data\Countries_and_continents_of_the_world.csv")
st.title("WORLD POPULATION")
# Add a button to view raw data
if st.button("View Raw Data"):
    st.write(countries [['Country Name', 'Infant mortality (per 1000 births)']])

# Create density mapbox plot
fig5 = px.density_mapbox(countries, lat='latitude', lon='longitude', z='Infant mortality (per 1000 births)',
                        radius=20, center=dict(lat=0, lon=0), zoom=0,
                        mapbox_style="open-street-map")


# Set title for the plot
fig5.update_layout(title="Infant mortality rate of the Countries")

# Display the plot in Streamlit
st.plotly_chart(fig5)


