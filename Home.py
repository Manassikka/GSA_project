import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
There are Total of 24 visulaization of Geospatial data using different kinds of visualizations like Markup Clusters,Heatmaps & Choropleth Maps
"""

st.sidebar.title("Pages")
st.sidebar.info(markdown)
logo = "https://imgs.search.brave.com/_OlvKYWp3pxgcVktNZ1E-VibONyiCsFhJhIxsLLVpLw/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9jZG4u/cGl4YWJheS5jb20v/cGhvdG8vMjAxMS8x/Mi8xMy8xNC8zMS9l/YXJ0aC0xMTAxNV82/NDAuanBn"
st.sidebar.image(logo)

# Customize page title
st.title("GEOSPATIAL ANALYSIS")

st.markdown(
    """
Geospatial analysis with Folium and Streamlit offers an interactive way to visualize and explore spatial data of India as well as of World, enabling users to gain insights and make informed decisions through dynamic maps and intuitive interfaces.

    """
)

st.header("Instructions")

markdown = """
1. For the [GitHub repository](https://github.com/opengeos/streamlit-map-template) or [use it as a template](https://github.com/opengeos/streamlit-map-template/generate) for your own project.
2. Customize the sidebar by changing the sidebar text and logo in each Python files.
3. Find your favorite emoji from https://emojipedia.org.
4. Add a new app to the `pages/` directory with an emoji in the file name, e.g., `1_🚀_Chart.py`.

"""

st.markdown(markdown)

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
