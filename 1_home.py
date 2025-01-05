import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col= 0)
    df_data = df_data[df_data['Contract Valid Until']>= 2023]
    df_data = df_data[df_data['Value(£)']> 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state['data'] = df_data

st.markdown("# Fifa 2023 Official Dataset")

btn = st.button("See data in Kaggle")
if btn:
    webbrowser.open_new_tab('https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database')

st.markdown(
    """
    The dataset is from Fifa players from 2017 to 2023
    """
)