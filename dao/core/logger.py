import logging

class Logger:
    """
    Centralized logger setup.
    Allows consistent logging throughout the application.
    """

    @staticmethod
    def setup_logger(name: str, level: str = "INFO"):
        logger = logging.getLogger(name)
        logger.setLevel(level)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger