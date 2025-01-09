import sqlite3

class ContributionHandler:
    def __init__(self, db_path="database/contributions.db"):
        self.db_path = db_path
        self._setup_database()

    def _setup_database(self):
        """Set up the database schema for contributions."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS contributions (
                    id INTEGER PRIMARY KEY,
                    user_id TEXT NOT NULL,
                    type TEXT NOT NULL,
                    amount REAL NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()

    def record_contribution(self, user_id, contribution_type, amount):
        """Records a new user contribution."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO contributions (user_id, type, amount) 
                VALUES (?, ?, ?)
            """, (user_id, contribution_type, amount))
            conn.commit()
        return {"status": "success", "message": "Contribution recorded"}

    def get_user_contributions(self, user_id):
        """Fetches all contributions of a specific user."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM contributions WHERE user_id = ?
            """, (user_id,))
            rows = cursor.fetchall()
        return rows