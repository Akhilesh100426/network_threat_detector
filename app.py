import streamlit as st
import pandas as pd
import joblib
import time
from datetime import datetime
import threading
import queue
from utils.feature_extraction_url import extract_features

# Load models
rf_url_model = joblib.load("model/rf_url_model.pkl")
rf_net_model, netflow_feature_cols = joblib.load("model/realtime_rf_model.pkl")

# Streamlit UI
st.set_page_config(page_title="Network Threat Detector", layout="wide")
st.title("🛡️ AI-Powered Network Threat Detector")

mode = st.radio("Choose Detection Mode:", ["URL-based (SQLi/XSS/Phishing)", "Live Network Traffic Monitoring (PyShark)"])

# 1️ URL Detection
if mode == "URL-based (SQLi/XSS/Phishing)":
    st.subheader("🔍 Detect Malicious URLs")
    option = st.radio("Choose Input Type:", ["Upload CSV", "Enter Single URL"])

    if option == "Upload CSV":
        uploaded_file = st.file_uploader("Upload a CSV file with a 'url' column", type=["csv"])
        if uploaded_file:
            df = pd.read_csv(uploaded_file)
            if "url" in df.columns:
                df["features"] = df["url"].apply(extract_features)
                df["prediction"] = df["features"].apply(lambda x: rf_url_model.predict([x])[0])
                df["result"] = df["prediction"].apply(lambda pred: "🟢 Benign" if pred == 0 else f"🔴 {str(pred).capitalize()}")
                st.dataframe(df[["url", "result"]])
            else:
                st.error("CSV must contain a column named 'url'")

    else:
        url = st.text_input("Enter a URL:")
        if url:
            features = extract_features(url)
            pred = rf_url_model.predict([features])[0]
            result = "🟢 Benign" if pred == 0 else f"🔴 {str(pred).capitalize()}"
            https_used = "Yes" if features[-1] == 1 else "No"
            st.markdown(f"### Prediction: {result}")
            st.markdown(f"**HTTPS used?** {https_used}")

elif mode == "Live Network Traffic Monitoring (PyShark)":
    import os
    from streamlit_autorefresh import st_autorefresh

    st.subheader("📡 Real-time Network Packet Monitoring")
    st.info("ℹ️ Make sure `utils/pyshark_packet_sniffer.py` is running in the background and writing to `logs/sniffer_output.txt`.")

  
    auto_refresh = st.checkbox("🔄 Auto-refresh every 2 seconds", value=True)
    if auto_refresh:
        st_autorefresh(interval=2000, limit=None, key="sniffer_autorefresh")

    
    if st.button("🧹 Clear Log"):
        try:
            open("logs/sniffer_output.txt", "w").close()
            st.success("✅ Log cleared.")
        except Exception as e:
            st.error(f"❌ Could not clear log: {e}")

    
    st.markdown("### 📋 Real-time Predictions")
    result_area = st.empty()

    def read_logs():
        try:
            with open("logs/sniffer_output.txt", "r") as f:
                lines = f.readlines()
                if not lines:
                    return ["🔎 Waiting for predictions..."]
                return lines[-20:]  
        except FileNotFoundError:
            return ["❌ Log file 'sniffer_output.txt' not found. Make sure the sniffer script is running."]

    logs = read_logs()
    result_area.code("".join(logs))
