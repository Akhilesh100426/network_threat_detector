# 🛡️ AI-Powered Network Threat Detector

This project is an AI-based real-time network threat detection system built using **machine learning**, **Streamlit**, and **PyShark**. It detects malicious packets in live traffic and classifies suspicious URLs (Phishing, SQLi, XSS).

---

## 📌 Features

- 🔗 **URL-based Threat Detection**  
  Detects malicious URLs using a trained Random Forest model.

- 📡 **Live Network Traffic Monitoring (PyShark)**  
  Captures and analyzes packets in real time using PyShark.

- 🔁 **Auto-Refreshing Log Viewer**  
  Streamlit auto-refreshes every 2 seconds to display live threat predictions.

---

## 📁 Project Structure

```
network-threat-detector/
├── app.py
├── logs/
│   └── sniffer_output.txt
├── model/
│   ├── realtime_rf_model.pkl
│   └── rf_url_model.pkl
├── utils/
│   ├── pyshark_packet_sniffer.py
│   ├── feature_extraction_url.py
│   ├── packet_capture.py
│   ├── train_realtime_model.py
│   └── train_url_model.py
└── *.csv  # Datasets
```

---

## 🚀 Getting Started

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

> Example `requirements.txt`:
> ```
> streamlit
> pyshark
> scapy
> joblib
> pandas
> ```

---

### 2️⃣ Train the Models (Optional)

```bash
python -m utils.train_url_model
python utils/train_realtime_model.py
```

---

### 3️⃣ Start Packet Sniffer

```bash
python utils/pyshark_packet_sniffer.py
```

> This writes predictions to `logs/sniffer_output.txt`.

---

### 4️⃣ Launch the Streamlit App

```bash
streamlit run app.py
```

---

## 🧠 ML Models

- `rf_url_model.pkl`: Predicts whether a URL is benign or contains SQLi/XSS/phishing.
- `realtime_rf_model.pkl`: Classifies live network packets as Benign or Malicious.

---

## 📽️ Demo Video

[![Watch Demo](https://img.shields.io/badge/📺%20Watch%20Demo-Google%20Drive-blue?logo=google-drive)](https://drive.google.com/file/d/1GU2YGVQ49JmRmidfRoLfJ3t4MLD4xuDh/view?usp=drivesdk)

👉 Click the badge or [watch the demo here](https://drive.google.com/file/d/1GU2YGVQ49JmRmidfRoLfJ3t4MLD4xuDh/view?usp=drivesdk)

---

## 🙋 Author

**GONGADI AKHILESH - BAVIGADDA MANI KUMAR REDDY - SIRIVELLA VAMSI KRISHNA**   
Intel Unnati Internship Project – *AI/ML for Networking*
