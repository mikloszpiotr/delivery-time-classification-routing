
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from scripts.visualization.plot_utils import plot_class_distribution

st.title("🔍 Data Exploration")

@st.cache_data
def load_data():
    return pd.read_csv("data/raw/delivery_data.csv")

df = load_data()
st.write("### Raw Data Preview", df.head())

st.write("### Class Distribution")
plot_class_distribution(df)

st.write("### Correlation Heatmap")
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
st.pyplot()
