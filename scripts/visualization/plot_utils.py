
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_class_distribution(df):
    sns.countplot(x='delivery_class', data=df)
    plt.title("Delivery Class Distribution")
    plt.xlabel("Class")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()
