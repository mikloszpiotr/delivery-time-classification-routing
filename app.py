
import streamlit as st
from pathlib import Path

# Redirect user to Home page
st.set_page_config(page_title="Delivery Time Classifier", layout="wide")

st.markdown(
    '''
    # 🚚 Delivery Time Classification & Routing App

    Use the sidebar to explore:
    - 📊 Data Exploration
    - 🤖 Model Training
    - 🚀 Prediction & Routing
    '''
)

st.info("Please select a page from the sidebar to get started.")
