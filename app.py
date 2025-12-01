# Import necessary libraries
import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load('movie_success_model.sav')

# Streamlit App Title
st.title("🎥 Movie Success Prediction App")

# Centered layout for better page fit
st.markdown(
    """
    <style>
    .block-container {
        max-width: 800px;
        padding-top: 1rem;
        padding-bottom: 1rem;
        margin: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🎬 Movie Input Section
st.header("📊 Enter Movie Details")

# Create columns for a 3x3 grid
col1, col2, col3 = st.columns(3)

# Define user input fields (Updated to use number_input for some)
with col1:
    year = st.number_input("📅 Year of Release", min_value=1980, max_value=2025, step=1, value=2015)
    rating = st.number_input("⭐ IMDB Rating", min_value=0.0, max_value=10.0, step=0.1, value=7.5)
    action = st.selectbox("💥 Action: No (0) / Yes (1)", [0, 1])

with col2:
    runtime = st.number_input("⏳ Runtime (Minutes)", min_value=60, max_value=300, step=1, value=120)
    votes = st.number_input("🗳️ Number of Votes", min_value=1000, max_value=1000000, step=1000, value=50000)
    adventure = st.selectbox("🚀 Adventure: No (0) / Yes (1)", [0, 1])

with col3:
    metascore = st.number_input("📈 Metascore", min_value=0, max_value=100, step=1, value=70)
    revenue = st.number_input("💰 Revenue (Millions)", min_value=0.1, max_value=1000.0, step=0.1, value=100.0)
    comedy = st.selectbox("😂 Comedy: No (0) / Yes (1)", [0, 1])

# Prepare input for prediction
input_data = np.array([
    year, runtime, rating, votes, revenue, metascore, action, adventure, comedy
]).reshape(1, -1)

# Predict button
if st.button("🎯 Predict Movie Success"):
    prediction = model.predict(input_data)[0]
    
    if prediction == 1.0:
        st.success("🎉 The movie is predicted to be a **HIT!**")
    else:
        st.error("😞 The movie is predicted to be a **FLOP.**")

