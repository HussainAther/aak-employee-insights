# streamlit_dashboard/employee_analyzer.py

import streamlit as st
import requests
import json

st.set_page_config(page_title="Employee Analyzer")
st.title("🧠 Employee Session Analyzer")

API_URL = "http://localhost:8000/api/analyze-session"

st.markdown("Enter session data and analyze alignment with assigned tasks.")

with st.form("session_form"):
    user_id = st.text_input("User ID", value="syedather")
    keyboard = st.slider("Total keystrokes", min_value=0, max_value=1000, value=150)
    mouse = st.slider("Total mouse movement (pixels)", min_value=0, max_value=10000, value=3000)
    window = st.selectbox("Active window", ["vscode", "chrome", "pycharm", "terminal"])
    duration = st.slider("Session duration (minutes)", min_value=1, max_value=120, value=30)
    submit = st.form_submit_button("Analyze")

if submit:
    session = {
        "keyboard_bursts": [{"keystrokes": keyboard}],
        "mouse_movements": [{"pixels": mouse}],
        "active_window": window,
        "duration_minutes": duration
    }

    payload = {"user_id": user_id, "session": session}
    res = requests.post(API_URL, json=payload)

    if res.ok:
        result = res.json()
        st.success("Analysis complete ✅")
        st.json(result)
    else:
        st.error("Failed to analyze session")
