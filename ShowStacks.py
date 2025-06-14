import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(layout="wide")
st.title("Japan EPCO Generation Stacked Graphs (2024)")

# 地域リストとファイル名
regions = [
    "Hokkaido", "Tohoku", "TEPCO", "Hokuriku", "Chubu",
    "Kansai", "Chugoku", "Shikoku", "Kyushu", "Okinawa"
]
file_map = {region: f"{region} 1.csv" for region in regions}

# 積み上げ対象列
main_cols = ['E', 'F', 'G', 'H', 'J', 'R']  # LNG, Coal, Oil, Biomass, Thermal_Other, PS
renew_cols = ['K', 'L', 'M']               # Solar, Wind, Hydro

# タブを分ける
tab1, tab2 = st.tabs(["Main Sources", "Renewables"])

# 共通：読み込みと表示関数
def plot_stacked(df, columns, title):
    fig, ax = plt.subplots(figsize=(10, 2))
    df[columns].plot.area(ax=ax, stacked=True)
    ax.set_title(title)
    ax.set_ylabel("Output")
    ax.set_xlabel("Time")
    st.pyplot(fig)

# Main Sources タブ
with tab1:
    st.subheader("Main Sources: LNG, Coal, Oil, Biomass, Thermal_Other, PS")
    for region in regions:
        st.markdown(f"### {region}")
        df = pd.read_csv(file_map[region])
        plot_stacked(df, main_cols, region)

# Renewables タブ
with tab2:
    st.subheader("Renewables: Solar, Wind, Hydro")
    for region in regions:
        st.markdown(f"### {region}")
        df = pd.read_csv(file_map[region])
        plot_stacked(df, renew_cols, region)
