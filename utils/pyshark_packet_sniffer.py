import pyshark
import joblib
import pandas as pd
import time
import os
from datetime import datetime

model_path = os.path.join("model", "realtime_rf_model.pkl")
rf_net_model, netflow_feature_cols = joblib.load(model_path)

os.makedirs("logs", exist_ok=True)
log_file_path = os.path.join("logs", "sniffer_output.txt")

def predict_packet(length):
    features = {
        "Flow Duration": 1,
        "Total Fwd Packets": 1,
        "Total Backward Packets": 1,
        "Flow Bytes/s": length,
        "Flow Packets/s": 1,
        "Fwd Packet Length Mean": length,
        "Bwd Packet Length Mean": length,
        "Packet Length Mean": length,
        "Packet Length Std": 0,
        "PSH Flag Count": 0,
        "ACK Flag Count": 0,
        "URG Flag Count": 0,
        "Fwd Packets/s": 1,
        "Avg Fwd Segment Size": length
    }

    df = pd.DataFrame([features])
    for col in netflow_feature_cols:
        if col not in df.columns:
            df[col] = 0
    df = df[netflow_feature_cols]
    pred = rf_net_model.predict(df)[0]
    return "Benign" if pred == 0 else "Malicious"

def start_sniffing(interface="Wi-Fi"):
    try:
        cap = pyshark.LiveCapture(interface=interface, bpf_filter="ip")

        print(f"[INFO] Starting packet capture on interface: {interface}")
        for pkt in cap.sniff_continuously():
            try:
                length = int(pkt.length)
                label = predict_packet(length)
                timestamp = datetime.now().strftime("%H:%M:%S")
                log_line = f"[{timestamp}] {label}\n"

                # Write to log file
                with open(log_file_path, "a") as log_file:
                    log_file.write(log_line)

                print(log_line.strip())

            except Exception as e:
                print(f"[ERROR] Packet processing failed: {e}")
    except Exception as e:
        print(f"[FATAL] Failed to start sniffing: {e}")

if __name__ == "__main__":
    start_sniffing(interface="Wi-Fi")  
