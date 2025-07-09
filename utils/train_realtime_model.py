# utils/train_realtime_model.py
import pandas as pd
import joblib
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load dataset
df = pd.read_csv("../Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv")

df.columns = df.columns.str.strip()

if "Label" not in df.columns:
    print("❌ 'Label' column not found! Available columns:")
    print(df.columns.tolist())
    exit()

df.replace([float("inf"), float("-inf")], 0, inplace=True)
df.dropna(inplace=True)

df["Label"] = df["Label"].apply(lambda x: 0 if str(x).strip().upper() == "BENIGN" else 1)

features = [
    "Flow Duration", "Total Fwd Packets", "Total Backward Packets", "Flow Bytes/s",
    "Flow Packets/s", "Fwd Packet Length Mean", "Bwd Packet Length Mean",
    "Packet Length Mean", "Packet Length Std", "PSH Flag Count", "ACK Flag Count",
    "URG Flag Count", "Fwd Packets/s", "Avg Fwd Segment Size"
]
available = [col for col in features if col in df.columns]
df = df[available + ["Label"]]

X = df.drop(columns=["Label"])
y = df["Label"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=50, max_depth=10, random_state=42)
model.fit(X_train, y_train)

print("📊 Classification Report:")
print(classification_report(y_test, model.predict(X_test)))

os.makedirs("../model", exist_ok=True)
joblib.dump((model, X.columns.tolist()), "model/realtime_rf_model.pkl")
print("✅ Model saved to ../model/realtime_rf_model.pkl")