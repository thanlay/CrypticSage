import sqlite3

def initialize_database():
    """Initializes the database schema."""
    with sqlite3.connect("database/system.db") as conn:
        cursor = conn.cursor()
        # Create Users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                user_id TEXT UNIQUE NOT NULL,
                balance REAL DEFAULT 0
            )
        """)
        # Create Transactions table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                sender TEXT NOT NULL,
                receiver TEXT NOT NULL,
                amount REAL NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()