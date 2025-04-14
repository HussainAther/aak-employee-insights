# 🔬 AAK Scientific Insights: Quadrangulation & Task Analysis

A full-stack behavioral intelligence platform for AAK Telscience, designed to monitor, analyze, and optimize employee performance using real-time activity data.

## 🚀 Features

### 🧠 Quadrangulation Engine
Combines four key data sources:
- ⌨️ Keyboard input
- 🖱️ Mouse activity
- 🪟 Screen context (active window)
- 🧠 Assigned task metadata

Outputs:
- ✅ Task Match Score
- 💡 Innovation Index
- ⚙️ System Efficiency
- 📈 Market Relevance

### 🧬 Real Employee Metadata
- Fetches live employee/project/task info from AAK's production PostgreSQL DB (via SSH or direct)
- Auto-matches user ID and task

### 📡 FastAPI Backend
- `POST /api/analyze-session` → returns full analysis
- Live testable Swagger docs at `http://localhost:8000/docs`

### 📊 Streamlit Frontend
- Sidebar-tabbed interface: Home + Employee Analyzer
- Interactive input for session activity
- Bar chart + metric breakdown
- Real-time recommendations based on behavior vs. assignment

### 🧠 Machine Learning
- Built-in classification model for task quality (`best_practice` vs `needs_improvement`)
- Extensible for content analysis and prompt-level evaluation

---

## 🧱 Project Structure

```
scientific-insights-app/
├── backend/
│   ├── main.py              # FastAPI entry point
│   ├── database.py          # PostgreSQL & SSH tunnel connection
│   ├── routers/             # API endpoints
│   │   └── analyze.py       # Analyze session route
├── tracking/
│   ├── session_analyzer.py  # Core logic for behavioral scoring
│   ├── session_tracker.py   # Simulated user session generator
│   ├── train_content_model.py # Innovation classifier
│   └── metadata_fetcher.py  # Pull employee data from AAK DB
├── streamlit_dashboard/
│   └── employee_analyzer.py # Frontend session input + results
├── settings.env             # DB + API secrets
├── ssh-tunnel-data.pem      # SSH key (private)
└── requirements.txt         # Dependencies
```

---

## ⚙️ How to Run (Local Demo)

### 1️⃣ Setup Environment
```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 2️⃣ Launch FastAPI
```bash
cd backend
uvicorn main:app --reload
# Visit: http://localhost:8000/docs
```

### 3️⃣ Launch Streamlit
```bash
cd streamlit_dashboard
streamlit run employee_analyzer.py
# Visit: http://localhost:8501
```

### 4️⃣ (Optional) SSH Tunnel
```bash
ssh -i .venv/ssh-tunnel-data.pem sshuser@18.211.208.120 -L 5433:database-1.cns565mcvpbw.us-east-1.rds.amazonaws.com:5432
```

---

## 📌 Notes
- Requires valid `.env` and `.pem` files for DB access
- Outputs and logs stored in `/data/sessions` (can be visualized)

---

## 🧪 Status Report Plan (coming soon)
- `GET /api/status-report` → roll-up of all users, recent sessions
- Trending charts and graphs
- Project/team-level behavioral summaries

---

## 💬 Contact
Syed Hussain Ather  
AI Engineer, AAK Telscience  
[hussainather.com](http://hussainather.com)

---

Let's revolutionize real-time scientific performance tracking. 🧠📊


