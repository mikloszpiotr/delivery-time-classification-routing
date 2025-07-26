
import streamlit as st
import numpy as np
from scripts.preprocessing.preprocess import preprocess_data
from sklearn.neighbors import KNeighborsClassifier

st.title("🚀 Predict Delivery Time Class")

# Input fields
weight = st.slider("Package Weight (kg)", 0.1, 20.0, 2.5)
distance = st.slider("Distance (km)", 1.0, 60.0, 10.0)
hour = st.slider("Pickup Hour", 0, 23, 9)
day = st.slider("Day of Week (0=Mon)", 0, 6, 1)
holiday = st.radio("Holiday?", [0, 1])

# Use default/average values for lat/lng inputs
pickup_lat = 51.0
pickup_lng = 20.0
dropoff_lat = 51.0
dropoff_lng = 20.0

# Match feature order from training
features = np.array([[pickup_lat, pickup_lng, dropoff_lat, dropoff_lng,
                      weight, distance, hour, day, holiday]])

# Load model (re-trained for demo simplicity)
X_train, X_test, y_train, y_test, scaler, le = preprocess_data("data/raw/delivery_data.csv")
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# Predict
scaled_features = scaler.transform(features)
prediction = model.predict(scaled_features)
class_name = le.inverse_transform(prediction)[0]

st.subheader(f"📦 Predicted Delivery Class: `{class_name.upper()}`")

if class_name == "fast":
    st.success("Route Suggestion: ✅ Assign to nearest courier")
elif class_name == "medium":
    st.warning("Route Suggestion: ⚠️ Consider dynamic re-routing")
else:
    st.error("Route Suggestion: 🛑 Schedule for later slot")
