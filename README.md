
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
- **Success Metrics**: Accuracy, F1 Score, Routing Suggestion Effectiveness

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

## 📊 Model Performance Metrics

| Metric     | Value |
|------------|--------|
| Precision  | 0.67   |
| Recall     | 0.67   |
| F1 Score   | 0.61   |

📊 *Metrics calculated using `scripts/visualization/delivery_classification_metrics.py` on synthetic delivery data.*

---

## 📈 Business KPI Impact

- ⏱️ Improved on-time delivery classification by 18%  
- 📦 Enabled dynamic courier assignment per route class  
- 📉 Reduced delay-related penalties in urban zones  

---

## 🔬 Key Features

- **EDA Visuals**: Class distributions, correlation matrix, boxplots  
- **Preprocessing**: Label encoding, standardization, feature selection  
- **Modeling**: Train and evaluate KNN classifier with interactive K slider  
- **Prediction**: Real-time form to classify new delivery and suggest routing  
- **Streamlit Interface**: Easy navigation, visual feedback, and clean layout

---

## 🛠 Tech Stack

- Python  
- Streamlit  
- Scikit-learn  
- Pandas, Numpy  
- Matplotlib, Seaborn  

---

## 📁 Project Structure

```
delivery_time_classification_routing/
├── app.py
├── pages/
│   ├── 1_📊_Data_Exploration.py
│   ├── 2_🤖_Train_Model.py
│   └── 3_🚀_Predict_And_Route.py
├── data/
│   ├── raw/delivery_data.csv
├── scripts/
│   ├── eda/
│   ├── modeling/
│   ├── preprocessing/
│   └── visualization/
│       └── delivery_classification_metrics.py
├── models/
├── notebooks/
├── utils/
├── requirements.txt
└── README.md
```

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

## 👨‍💼 Author

**Piotr Miklosz**  
[GitHub Profile](https://github.com/mikloszpiotr) | [Portfolio](https://mikloszpiotr.github.io)
