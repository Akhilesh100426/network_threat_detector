import os
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from utils.feature_extraction_url import extract_features  

# Load dataset
df = pd.read_csv("malicious_phish.csv") 

df = df.dropna(subset=["url", "type"])

X = [extract_features(url) for url in df["url"]]

y = [0 if label.lower() == "benign" else 1 for label in df["type"]]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Classification Report:\n")
print(classification_report(y_test, y_pred))

os.makedirs("model", exist_ok=True)

joblib.dump(model, "model/rf_url_model.pkl")
print("✅ Model saved to ../model/rf_url_model.pkl")
