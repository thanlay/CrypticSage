import os
from typing import Any, Dict


class Config:
    """
    Centralized configuration management.
    Allows for both environment variable and default value-based configurations.
    """

    DEFAULTS: Dict[str, Any] = {
        "TOKEN_CONTRACT_ADDRESS": "0x1234567890ABCDEF1234567890ABCDEF12345678",
        "BLOCKCHAIN_RPC_URL": "http://localhost:8545",
        "DATABASE_URI": "sqlite:///incentive_module.db",
        "LOG_LEVEL": "INFO",
    }

    @classmethod
    def get(cls, key: str, default=None) -> Any:
        """
        Retrieve a configuration value.
        :param key: Configuration key
        :param default: Default value if key is not set
        :return: Configured value
        """
        return os.getenv(key, cls.DEFAULTS.get(key, default))