import streamlit as st
import webbrowser

st.markdown("# Fifa 2023 Official Dataset")

btn = st.button("See data in Kaggle")
if btn:
    webbrowser.open_new_tab('https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database')

st.markdown(
    """
    The dataset is from Fifa players from 2017 to 2023
    """
)