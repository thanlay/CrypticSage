import hashlib
import hmac
import re

class SecurityLayer:
    def __init__(self, secret_key="default_secret_key"):
        self.secret_key = secret_key

    def hash_data(self, data):
        """Hashes the given data using SHA256."""
        return hashlib.sha256(data.encode()).hexdigest()

    def validate_input(self, input_data, pattern):
        """Validates input data against a regex pattern."""
        return re.match(pattern, input_data) is not None

    def sign_message(self, message):
        """Signs a message using HMAC with a secret key."""
        return hmac.new(self.secret_key.encode(), message.encode(), hashlib.sha256).hexdigest()

    def verify_signature(self, message, signature):
        """Verifies the HMAC signature of a message."""
        return hmac.compare_digest(self.sign_message(message), signature)