import streamlit as st

st.title("🌍 GIS Automation Tool")
st.write("App is running successfully ✅")

# Button to trigger analysis
if st.button("Run Analysis"):

    st.write("Running analysis...")

    hospitals = gpd.read_file("hospitals.shp")
    schools = gpd.read_file("schools.shp")

    # Convert CRS
    hospitals = hospitals.to_crs(epsg=3857)
    schools = schools.to_crs(epsg=3857)

    # Buffer
    hospitals["geometry"] = hospitals.buffer(1000)

    # Spatial join
    result = gpd.sjoin(schools, hospitals, how="inner", predicate="intersects")

    st.success("✅ Analysis Completed!")

    # Show output
    st.dataframe(result)

    # Download option
    csv = result.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download CSV", csv, "result.csv", "text/csv")