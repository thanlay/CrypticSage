import os
from typing import Dict

class Config:
    """
    Global configuration management.
    Allows easy extension for environment variables and external configs.
    """
    DEFAULTS = {
        "BLOCKCHAIN_RPC_URL": "http://localhost:8545",
        "DAO_CONTRACT_ADDRESS": "0x1234567890ABCDEF1234567890ABCDEF12345678",
        "LOG_LEVEL": "INFO",
    }

    @classmethod
    def get(cls, key: str, default=None):
        """
        Get a configuration value.
        First checks environment variables, then defaults.
        """
        return os.getenv(key, cls.DEFAULTS.get(key, default))

    @classmethod
    def all(cls) -> Dict[str, str]:
        """Return all configuration values."""
        return {key: cls.get(key) for key in cls.DEFAULTS}