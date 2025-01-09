import logging
from datetime import datetime

class AuditLogger:
    def __init__(self, log_file="audit.log"):
        """
        Initialize the audit logger.
        """
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )

    def log_notification(self, recipient, notification_type, status, message=None):
        """
        Log a notification event.
        """
        logging.info(
            f"Recipient: {recipient}, Type: {notification_type}, Status: {status}, Message: {message}"
        )


# Example Usage
if __name__ == "__main__":
    audit_logger = AuditLogger()
    audit_logger.log_notification(
        recipient="user@example.com",
        notification_type="email",
        status="success",
        message="Email sent successfully.",
    )
    audit_logger.log_notification(
        recipient="+1234567890",
        notification_type="sms",
        status="failed",
        message="Network error occurred.",
    )