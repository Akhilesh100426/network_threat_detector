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

2. ▶️ Run train_url_model.py
  python -m utils.train_url_model

3. ▶️ Start Packet Sniffer (PyShark-based)
  python utils/pyshark_packet_sniffer.py
  This writes predictions to: logs/sniffer_output.txt

4. 🖥️ Launch Streamlit UI
  streamlit run app.py

🧠 Models
rf_url_model.pkl: Predicts whether a URL is benign or contains SQLi/XSS/phishing patterns.
realtime_rf_model.pkl: Classifies real-time packets as Benign or Malicious.

## 📽️ Demo Video

[![Watch Demo](https://img.youtube.com/vi/VIDEO_ID/maxresdefault.jpg)](https://drive.google.com/file/d/1GU2YGVQ49JmRmidfRoLfJ3t4MLD4xuDh/view?usp=drivesdk)

👉 Click the image or [watch the demo](https://drive.google.com/file/d/1GU2YGVQ49JmRmidfRoLfJ3t4MLD4xuDh/view?usp=drivesdk) on Google Drive.



