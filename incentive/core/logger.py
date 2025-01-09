import logging

class Logger:
    def __init__(self, log_file="logs/system.log"):
        """Initializes the logging configuration."""
        self.logger = logging.getLogger("ApplicationLogger")
        self.logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler(log_file)
        console_handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def log_info(self, message):
        """Logs an informational message."""
        self.logger.info(message)

    def log_error(self, message):
        """Logs an error message."""
        self.logger.error(message)

    def log_debug(self, message):
        """Logs a debug message."""
        self.logger.debug(message)

    def log_warning(self, message):
        """Logs a warning message."""
        self.logger.warning(message)