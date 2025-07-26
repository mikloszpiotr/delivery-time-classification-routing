# 🚚 Delivery Time Classification & Dynamic Routing

This end-to-end Machine Learning project demonstrates how to classify delivery orders based on estimated delivery time and provide smart routing suggestions. It's designed as a portfolio project using a modular, scalable structure and Streamlit for deployment.

---

## 📌 Business Problem

In logistics and e-commerce, it is critical to forecast delivery speed (fast/medium/slow) to:
- Optimize courier assignment
- Enable real-time route reallocation
- Improve customer satisfaction
- Reduce operational cost and delay penalties

---

## 🎯 Objective

- **Task Type**: Classification  
- **Target Variable**: `delivery_class` (`fast`, `medium`, `slow`)  
- **Success Metrics**: Accuracy, Confusion Matrix, Routing Suggestion Strategy  

---

## 🧠 Machine Learning Approach

- **Model Used**: K-Nearest Neighbors (KNN)  
- **Why KNN?** Simple, explainable, distance-based classifier suitable for early-stage deployment.  
- **Input Features**:
  - Pickup & dropoff coordinates
  - Package weight
  - Distance (km)
  - Pickup hour
  - Day of week
  - Holiday flag

---

## 📁 Project Structure

```
delivery_time_classification_routing/
│
├── app.py                             # Main Streamlit app
├── pages/                             # Streamlit pages
│   ├── 1_📊_Data_Exploration.py
│   ├── 2_🤖_Train_Model.py
│   └── 3_🚀_Predict_And_Route.py
│
├── data/
│   ├── raw/delivery_data.csv          # Synthetic delivery dataset
│   └── processed/                     # Placeholder for transformed data
│
├── scripts/
│   ├── eda/eda.py
│   ├── preprocessing/preprocess.py
│   ├── modeling/train_knn.py
│   └── visualization/plot_utils.py
│
├── models/                            # Trained model artifacts (optional)
├── notebooks/                         # EDA and test notebooks
├── utils/                             # Helper functions
├── requirements.txt                   # Project dependencies
└── README.md                          # Project overview and instructions
```

---

## 🔬 Key Features

- **EDA Visuals**: Class distributions, correlation matrix, boxplots
- **Preprocessing**: Label encoding, standardization, feature selection
- **Modeling**: Train and evaluate KNN classifier with interactive K slider
- **Prediction**: Real-time form to classify new delivery and suggest routing
- **Streamlit Interface**: Easy navigation, visual feedback, and clean layout

---

## 🚀 How to Run This App

### 🔧 1. Install Requirements

```bash
pip install -r requirements.txt
```

### ▶️ 2. Launch Streamlit App

```bash
streamlit run app.py
```

---

## 📊 Sample Prediction Logic

Based on model output:
- `fast`: ✅ Assign to nearest courier
- `medium`: ⚠️ Consider dynamic re-routing
- `slow`: 🛑 Schedule for off-peak delivery

---

## 🛠 Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas, Numpy
- Matplotlib, Seaborn

---

## 📈 Future Improvements

- Replace KNN with more robust classifiers (RandomForest, LightGBM)
- Include geospatial clustering (H3, DBSCAN)
- Use real-time traffic and weather data
- Save/load trained models with `joblib`
- Integrate with delivery APIs (e.g., HERE, Google Maps)

---

## 👨‍💼 Author

**Piotr Miklosz**  
[GitHub Profile](https://github.com/mikloszpiotr) | [Portfolio](https://mikloszpiotr.github.io)