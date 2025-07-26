
import streamlit as st

st.set_page_config(page_title="Delivery Time Classification", layout="wide")

st.title("🚚 Delivery Time Classification & Dynamic Routing")
st.markdown("""
Welcome to the **Delivery Time Classification** project.  
This tool helps classify deliveries into **fast**, **medium**, and **slow** buckets using a KNN model.

👨‍💻 Steps covered:
- Data Cleaning & Exploration  
- Preprocessing & Feature Engineering  
- Model Training with KNN  
- Delivery Prediction & Routing Suggestion

Use the sidebar to explore each part of the app.
""")
