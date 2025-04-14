# tracking/session_tracker.py

import time
import random
from datetime import datetime


def simulate_user_activity(duration_seconds=60):
    """
    Simulate a user's keyboard and mouse activity during a coding session.
    Returns a dictionary with timestamps, bursts, and dominant windows.
    """
    session = {
        "start_time": str(datetime.utcnow()),
        "keyboard_bursts": [],
        "mouse_movements": [],
        "active_window": "vscode",
        "duration_minutes": duration_seconds / 60.0
    }

    for second in range(duration_seconds):
        # Simulate keyboard typing burst
        if random.random() < 0.3:
            session["keyboard_bursts"].append({
                "timestamp": time.time(),
                "keystrokes": random.randint(3, 20)
            })

        # Simulate mouse movement
        if random.random() < 0.5:
            session["mouse_movements"].append({
                "timestamp": time.time(),
                "pixels": random.randint(10, 500)
            })

        time.sleep(0.05)  # fast simulation (not real time)

    session["end_time"] = str(datetime.utcnow())
    return session


if __name__ == "__main__":
    test_session = simulate_user_activity(10)
    from pprint import pprint
    pprint(test_session)

