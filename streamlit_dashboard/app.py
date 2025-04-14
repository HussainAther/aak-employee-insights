# streamlit_dashboard/app.py

import streamlit as st
import requests
import json

API_BASE = "http://localhost:8000"

st.set_page_config(page_title="AAK Insights Dashboard")
st.title("🧠 AAK Employee Insights")

view = st.sidebar.selectbox("Choose a View", ["Home", "Employee Analyzer"])

if view == "Home":
    st.markdown("Welcome to the AAK Behavioral Intelligence System.")

elif view == "Employee Analyzer":
    st.header("🔍 Employee Session Analyzer")

    mode = st.radio("Choose input mode:", ["Simulate Session", "Upload Session JSON"])

    user_id = st.text_input("Enter user ID (e.g., syedather)", value="syedather")

    session_data = None

    if mode == "Simulate Session" and st.button("Simulate and Analyze"):
        res = requests.get(f"{API_BASE}/api/simulate-and-analyze")
        if res.ok:
            session_data = res.json()

    elif mode == "Upload Session JSON":
        uploaded_file = st.file_uploader("Upload session JSON file")
        if uploaded_file is not None:
            try:
                session_json = json.load(uploaded_file)
                payload = {"user_id": user_id, "session": session_json}
                res = requests.post(f"{API_BASE}/api/analyze-session", json=payload)
                if res.ok:
                    session_data = res.json()
                else:
                    st.error(res.text)
            except Exception as e:
                st.error(f"Error reading file: {e}")

    if session_data:
        st.success("✅ Analysis Complete")
        st.metric("Task Match Score", f"{session_data['task_match_score'] * 100:.1f}%")
        st.write("**Status:**", session_data["status"])
        st.write("**Recommendations:**")
        for rec in session_data["recommendations"]:
            st.write(f"- {rec}")

