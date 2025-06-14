import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(layout="wide")
st.title("Japan EPCO Generation Stacked Graphs (2024)")

regions = [
    "Hokkaido", "Tohoku", "TEPCO", "Hokuriku", "Chubu",
    "Kansai", "Chugoku", "Shikoku", "Kyushu", "Okinawa"
]

file_map = {region: f"{region} 1.csv" for region in regions}

main_cols = ['E', 'F', 'G', 'H', 'J', 'R']  # LNG, Coal, Oil, Biomass, Thermal_Other, PS
renew_cols = ['K', 'L', 'M']               # Solar, Wind, Hydro

tab1, tab2 = st.tabs(["Main Sources", "Renewables"])

def plot_stacked(df, columns, title):
    fig, ax = plt.subplots(figsize=(10, 2))
    df[columns].plot.area(ax=ax, stacked=True)
    ax.set_title(title)
    ax.set_ylabel("Output")
    ax.set_xlabel("Time")
    st.pyplot(fig)

with tab1:
    st.subheader("Main Sources: LNG, Coal, Oil, Biomass, Thermal_Other, PS")
    for region in regions:
        st.markdown(f"### {region}")
        try:
            df = pd.read_csv(file_map[region])
            plot_stacked(df, main_cols, region)
        except:
            st.warning(f"{file_map[region]} が見つかりません")

with tab2:
    st.subheader("Renewables: Solar, Wind, Hydro")
    for region in regions:
        st.markdown(f"### {region}")
        try:
            df = pd.read_csv(file_map[region])
            plot_stacked(df, renew_cols, region)
        except:
            st.warning(f"{file_map[region]} が見つかりません")
