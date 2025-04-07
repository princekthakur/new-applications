# app.py
import streamlit as st
from scraper import scrape_player_stats
from model import predict_points

st.title("Dream11 Predictor")
team1 = st.selectbox("Select Team 1", ["MI", "CSK", "RCB"])
# ... (rest of your code)

if __name__ == "__main__":
    st.run()  # Or your custom logic
