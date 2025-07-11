# 🛡️ AI-Powered Network Threat Detector

This project is an AI-based real-time network threat detection system built using **machine learning**, **Streamlit**, and **PyShark**. It can detect malicious packets on live traffic and classify suspicious URLs (Phishing, SQLi, XSS).

---

## 📌 Features

- 🔗 **URL-based Threat Detection**  
  Detects malicious URLs via a trained ML model (Random Forest).

- 📡 **Live Network Traffic Monitoring (PyShark)**  
  Captures packets in real-time, extracts features, and detects malicious activity.

- 📋 **Auto-Refreshing Log Viewer**  
  Streamlit app auto-refreshes every 2 seconds to show real-time predictions from live sniffing.

---

## 📁 Project Structure

network-threat-detector/
├── app.py # Streamlit app
├── logs/
│ └── sniffer_output.txt # Live packet predictions (auto-updated)
├── model/
│ ├── realtime_rf_model.pkl # Trained model for live packet detection
│ └── rf_url_model.pkl # Trained model for URL detection
├── utils/
│ ├── pyshark_packet_sniffer.py # Live packet sniffer using PyShark
│ ├── feature_extraction_url.py # URL feature extraction
│ ├── packet_capture.py # (Optional) Scapy-based sniffer
│ ├── train_realtime_model.py # Script to train packet ML model
│ └── train_url_model.py # Script to train URL model
└── *.csv # training/test datasets


---

## 🚀 How to Run

### 1. 🔧 Install Dependencies


pip install -r requirements.txt
<details> <summary>Example <code>requirements.txt</code> entries:</summary>
streamlit
pyshark
scapy
joblib
pandas


