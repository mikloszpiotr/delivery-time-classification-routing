
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

def preprocess_data(data_path):
    df = pd.read_csv(data_path)
    df = df.drop(columns=['order_id'])

    # Encode labels
    le = LabelEncoder()
    df['delivery_class'] = le.fit_transform(df['delivery_class'])

    X = df.drop(columns=['delivery_time_min', 'delivery_class'])
    y = df['delivery_class']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test, scaler, le
