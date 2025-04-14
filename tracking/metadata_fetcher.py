# tracking/metadata_fetcher.py

import psycopg2
import os
from dotenv import load_dotenv
from tracking.database import get_connection

load_dotenv()

def fetch_employee_task_metadata():
    """
    Fetch real employee metadata from the AAK PostgreSQL database.
    Requires working .env and optionally uses SSH tunneling.
    """
    conn, tunnel = get_connection()
    if not conn:
        return []

    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT username, name, team, role, project_id, expected_task
            FROM employee_task_assignments
            LIMIT 100;
        """)
        columns = [desc[0] for desc in cur.description]
        rows = [dict(zip(columns, row)) for row in cur.fetchall()]
        cur.close()
        return rows

    except Exception as e:
        print("[Metadata Fetch Error]", e)
        return []

    finally:
        conn.close()
        if tunnel:
            tunnel.close()


# 🤖 Example call
if __name__ == "__main__":
    from pprint import pprint
    pprint(fetch_employee_task_metadata())

