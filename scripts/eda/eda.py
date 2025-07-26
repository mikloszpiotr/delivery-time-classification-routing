
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def run_eda(data_path):
    df = pd.read_csv(data_path)
    print("🔍 Basic Info:")
    print(df.info())
    print("\n📊 Summary Statistics:")
    print(df.describe())

    print("\n🧾 Class Distribution:")
    print(df['delivery_class'].value_counts())

    sns.countplot(x='delivery_class', data=df)
    plt.title("Delivery Time Class Distribution")
    plt.show()

    sns.boxplot(x='delivery_class', y='distance_km', data=df)
    plt.title("Distance by Delivery Class")
    plt.show()

    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.show()
