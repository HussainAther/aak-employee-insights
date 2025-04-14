# 🧠 AAK Employee Insights Engine

A full-stack behavioral intelligence pipeline powering AAK Telescience and Alter Learning's next-generation scientific and educational platforms.

This system quadrangulates developer activity — tracking keyboard/mouse behavior, screen context, and assigned tasks — to evaluate productivity, adherence to best practices, and recommend optimal project fit.

---

## 🚀 What It Does

- ⌨️ Tracks real-time keyboard & mouse activity
- 🧠 Analyzes whether developers are working on assigned tasks
- 🧪 Scores code sessions for best practices (modularity, testing, structure)
- 📈 Generates a match score between behavior and expected output
- 💼 Recommends employees for future roles or assignments
- 🌐 Powers investor, patent, and project recommendation layers across AAK & Alter Learning

---

## 📂 Project Structure

```
aak-employee-insights/
├── tracking/
│   ├── metadata_fetcher.py         # Normalized employee/project/task data
│   ├── session_tracker.py          # Tracks user behavior
│   ├── session_analyzer.py         # Scores session alignment & code practices
│   └── train_content_model.py      # Behavior tagging + LLM scoring
├── api/
│   └── main.py                     # FastAPI API for session ingestion and analysis
├── tests/
│   └── test_simulated_session.py   # End-to-end mock simulation test
├── data/
│   └── sessions/                   # Saved logs of session activity
├── README.md
├── requirements.txt
└── .env.example
```

---

## 🛠️ Getting Started

```bash
git clone https://github.com/aak-science/aak-employee-insights.git
cd aak-employee-insights
pip install -r requirements.txt
```

Then run the FastAPI backend:

```bash
uvicorn api.main:app --reload
```

---

## 🔁 Sample API Usage

```http
POST /api/analyze-session
```

```json
{
  "user_id": "aakriti_singh",
  "task_name": "Integrate geospatial APIs",
  "session": {
    "mouse": "high",
    "keyboard_bursts": 12,
    "active_window": "vscode",
    "duration_minutes": 45
  }
}
```

Returns:

```json
{
  "task_match_score": 0.91,
  "status": "on-task",
  "recommendations": [
    "Assign to map-patent feature",
    "Invite to AI data pipeline working group"
  ]
}
```

---

## 🧠 Project Goals

- Bring clarity and accountability to high-impact scientific projects
- Build trust with investors through real behavioral data
- Enhance team synergy by aligning people with the work they’re best at
- Lay the groundwork for global scientific collaboration

---

## 👥 Core Team

- **Syed Hussain Ather** — AI Engineer, Infrastructure Lead  
- **Aldi Agaj** — CEO, Strategic Vision  
- **Aakriti Singh** — Scientific Intelligence  
- **Bhuvaneswari R** — Data & Systems Integration  
- **Lautaro Rivera** — Developer Operations

---

## 🌍 Built For

- AAK Telescience – [aakscience.com](https://aakscience.com)  
- Alter Learning – [alter-learning.com](https://alter-learning.com)

---

## 🏁 Status

> MVP in active development — demo-ready prototype launching April 2025  
> Full integration with AAK and Alter Learning data pipelines in progress
