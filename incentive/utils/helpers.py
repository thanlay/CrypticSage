import datetime
import uuid

def generate_transaction_id():
    """Generates a unique transaction ID."""
    return str(uuid.uuid4())

def get_current_timestamp():
    """Gets the current timestamp in ISO format."""
    return datetime.datetime.utcnow().isoformat()

def validate_email(email):
    """Validates an email address format."""
    import re
    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return re.match(pattern, email) is not None