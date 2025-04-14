# tracking/session_analyzer.py

import os
import json
from tracking.metadata_fetcher import fetch_employee_task_metadata
from tracking.train_content_model import train_behavior_model
from tracking.utils import timestamp, save_session_log, load_session_log

# Load model once globally
model = train_behavior_model()

SESSION_LOG_PATH = "data/sessions"

def quadrangulate(session, task):
    """
    Perform quadrangulation using:
    1. Keyboard activity
    2. Mouse movement
    3. Screen capture (active window)
    4. Task name
    """
    activity_score = 0
    total_keystrokes = sum(burst["keystrokes"] for burst in session.get("keyboard_bursts", []))
    total_mouse = sum(m["pixels"] for m in session.get("mouse_movements", []))
    active_window = session.get("active_window", "")

    if total_keystrokes > 100:
        activity_score += 0.4
    if total_mouse > 2000:
        activity_score += 0.2
    if active_window.lower() in ["vscode", "pycharm"]:
        activity_score += 0.2
    if "test" in task or "evaluate" in task:
        activity_score += 0.2

    return round(activity_score, 2)

def analyze_session(user_id, session):
    """
    Quadrangulates user behavior from:
    - Keyboard
    - Mouse
    - Screen context (active window)
    - Task metadata

    And returns match score, innovation, efficiency, and market relevance indexes.
    Saves history for longitudinal tracking.
    """
    metadata = fetch_employee_task_metadata()
    user_record = next((u for u in metadata if u["user_id"] == user_id), None)

    if not user_record:
        return {"status": "error", "message": f"User {user_id} not found."}

    task = user_record["expected_task"].lower()
    project_id = user_record["project_id"].lower()
    duration = session.get("duration_minutes", 1)
    active_window = session.get("active_window", "")

    match_score = quadrangulate(session, task)

    # Innovation index (using text classification)
    sample_text = "Simulated session involving testing and clean code structure."
    innovation_prediction = model.predict([sample_text])[0]
    innovation_index = 1.0 if innovation_prediction == "best_practice" else 0.4

    # System efficiency index
    total_keystrokes = sum(burst["keystrokes"] for burst in session.get("keyboard_bursts", []))
    total_mouse = sum(m["pixels"] for m in session.get("mouse_movements", []))
    keystroke_density = total_keystrokes / duration
    mouse_density = total_mouse / duration
    focus_bonus = 1.0 if active_window.lower() == "vscode" else 0.8
    efficiency_index = round(min((keystroke_density + mouse_density) / 500 * focus_bonus, 1.0), 2)

    # Market relevance index (naive keyword matching for now)
    keywords = ["investor", "ai", "map", "science", "patent"]
    market_relevance_index = 0.9 if any(k in task for k in keywords) else 0.5

    # Load past logs for rolling avg (simple demo with last 3)
    history_files = [f for f in os.listdir(SESSION_LOG_PATH) if user_id in f][-3:]
    history_scores = []
    for f in history_files:
        log = load_session_log(os.path.join(SESSION_LOG_PATH, f))
        if "task_match_score" in log:
            history_scores.append(log["task_match_score"])

    rolling_avg = round(sum(history_scores[-3:]) / len(history_scores), 2) if history_scores else None
    delta = round(match_score - rolling_avg, 2) if rolling_avg is not None else None

    result = {
        "user_id": user_id,
        "task": task,
        "task_match_score": match_score,
        "task_match_score_rolling_avg": rolling_avg,
        "delta_vs_avg": delta,
        "innovation_index": round(innovation_index, 2),
        "efficiency_index": efficiency_index,
        "market_relevance_index": market_relevance_index,
        "status": "on-task" if match_score >= 0.7 else "review",
        "recommendations": [
            "Continue current assignment" if match_score >= 0.7 else "Needs review"
        ],
        "timestamp": timestamp()
    }

    save_session_log(user_id, result)
    return result


# 🤖 Example test run
if __name__ == "__main__":
    from tracking.session_tracker import simulate_user_activity
    sample = simulate_user_activity(10)
    result = analyze_session("syedather", sample)
    from pprint import pprint
    pprint(result)

