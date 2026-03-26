import streamlit as st
import geopandas as gpd

st.title("🌍 GIS Automation Tool")

st.write("Click the button to run analysis")

if st.button("Run Analysis"):

    st.write("Running analysis...")

    hospitals = gpd.read_file("hospitals.shp")
    schools = gpd.read_file("schools.shp")

    hospitals = hospitals.to_crs(epsg=3857)
    schools = schools.to_crs(epsg=3857)

    hospitals["geometry"] = hospitals.buffer(1000)

    result = gpd.sjoin(schools, hospitals, how="inner", predicate="intersects")

    st.success("✅ Done!")

    st.dataframe(result)