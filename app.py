import streamlit as st
import pandas as pd

st.title("🌍 GIS Automation Tool")

if st.button("Run Analysis"):

    df = pd.read_csv("result.csv")

    st.success("✅ Analysis Completed!")

    st.dataframe(df)

    # Show map (if lat/lon present)
    if "geometry" in df.columns:
        st.write("Map preview coming soon...")

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download CSV", csv, "result.csv", "text/csv")