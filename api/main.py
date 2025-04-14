# api/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from tracking.session_analyzer import analyze_session
from tracking.session_tracker import simulate_user_activity

app = FastAPI()

# ---- Models ----
class SessionData(BaseModel):
    user_id: str
    session: dict


@app.get("/")
def root():
    return {"message": "AAK Employee Insights API is live."}


@app.post("/api/analyze-session")
def analyze(session_data: SessionData):
    result = analyze_session(session_data.user_id, session_data.session)
    if result.get("status") == "error":
        raise HTTPException(status_code=404, detail=result["message"])
    return result


# 🧪 For quick testing
@app.get("/api/simulate-and-analyze")
def simulate():
    session = simulate_user_activity(10)
    return analyze_session("syedather", session)

