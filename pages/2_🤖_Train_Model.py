
import streamlit as st
from scripts.preprocessing.preprocess import preprocess_data
from scripts.modeling.train_knn import train_knn

st.title("🧠 Train KNN Classifier")

st.write("This page allows you to train a K-Nearest Neighbors classifier.")

data_path = "data/raw/delivery_data.csv"
X_train, X_test, y_train, y_test, _, _ = preprocess_data(data_path)

k = st.slider("Select K (neighbors)", min_value=1, max_value=15, value=5)

if st.button("Train Model"):
    model = train_knn(X_train, X_test, y_train, y_test, n_neighbors=k)
    st.success("Model trained and evaluated.")
