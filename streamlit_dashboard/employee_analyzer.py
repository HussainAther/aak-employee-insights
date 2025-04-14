# streamlit_dashboard/employee_analyzer.py

import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Scientific Insights Dashboard")
st.title("🔬 Scientific Insights Dashboard")

API_URL = "http://localhost:8000/api/analyze-session"

# Sidebar navigation
option = st.sidebar.selectbox(
    "Choose a view", [
        "Home",
        "Employee Analyzer"
    ]
)

if option == "Home":
    st.markdown("Welcome to the AAK Telscience Behavioral Intelligence System.")

elif option == "Employee Analyzer":
    st.header("🧠 Session Quadrangulation + Scoring")
    st.markdown("Enter session data to analyze user-task alignment in real time.")

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
            st.success("✅ Analysis complete")

            st.subheader("📊 Key Indices")
            metrics = pd.DataFrame({
                "Metric": ["Match Score", "Innovation", "Efficiency", "Market Relevance"],
                "Value": [
                    result.get("task_match_score", 0),
                    result.get("innovation_index", 0),
                    result.get("efficiency_index", 0),
                    result.get("market_relevance_index", 0)
                ]
            })
            st.dataframe(metrics.set_index("Metric"))

            chart = px.bar(metrics, x="Metric", y="Value", title="Session Analysis Breakdown")
            st.plotly_chart(chart, use_container_width=True)

            st.subheader("🧠 Recommendations")
            for rec in result.get("recommendations", []):
                st.markdown(f"- {rec}")

            st.caption(f"📅 Timestamp: {result.get('timestamp')}")

        else:
            st.error("Failed to analyze session")

