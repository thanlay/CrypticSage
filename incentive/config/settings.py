import os

class Config:
    """Configuration settings for the application."""
    DATABASE_URI = os.getenv("DATABASE_URI", "database/system.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    LOG_FILE = os.getenv("LOG_FILE", "logs/system.log")
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    TOKEN_REWARD_RATE = float(os.getenv("TOKEN_REWARD_RATE", 0.05))