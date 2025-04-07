import streamlit as st
import pandas as pd

st.title("🏏 Dream11 Fantasy Predictor")
st.write("Predict player points for today's match!")

# Example: Display a sample prediction table
sample_data = {
    "Player": ["Virat Kohli", "Jasprit Bumrah", "Rohit Sharma"],
    "Predicted Points": [72, 58, 65]
}
df = pd.DataFrame(sample_data)
st.dataframe(df)
