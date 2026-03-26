import streamlit as st
import pandas as pd

st.title("🌍 GIS Automation Tool")

st.write("Find schools near hospitals")

if st.button("Run Analysis"):

    st.write("Loading data...")

    # Load preprocessed result
    df = pd.read_csv("result.csv")

    st.success("✅ Analysis Completed!")

    st.dataframe(df)

    # Download option
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download CSV", csv, "result.csv", "text/csv")