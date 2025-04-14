# api/routes/analyze.py

from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, Any
from tracking.session_analyzer import analyze_session

router = APIRouter()

class SessionAnalysisRequest(BaseModel):
    user_id: str
    session: Dict[str, Any]

@router.post("/api/analyze-session")
def analyze_session_endpoint(request: SessionAnalysisRequest):
    """
    Accepts a user ID and a session dictionary, returns analysis output.
    """
    return analyze_session(request.user_id, request.session)
