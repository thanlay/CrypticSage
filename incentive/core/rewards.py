import sqlite3

class RewardProcessor:
    def __init__(self, db_path="database/rewards.db"):
        self.db_path = db_path
        self._setup_database()

    def _setup_database(self):
        """Set up the database schema for rewards."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS rewards (
                    id INTEGER PRIMARY KEY,
                    user_id TEXT NOT NULL,
                    amount REAL NOT NULL,
                    reason TEXT NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()

    def issue_reward(self, user_id, amount, reason="General Contribution"):
        """Issues a reward to a user."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO rewards (user_id, amount, reason)
                VALUES (?, ?, ?)
            """, (user_id, amount, reason))
            conn.commit()
        return {"status": "success", "message": f"Reward of {amount} issued to {user_id}"}

    def get_user_rewards(self, user_id):
        """Fetches reward history of a user."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM rewards WHERE user_id = ?
            """, (user_id,))
            rows = cursor.fetchall()
        return rows