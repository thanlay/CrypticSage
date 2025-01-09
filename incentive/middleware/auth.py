from flask import request, jsonify
from core.security import SecurityLayer

class AuthMiddleware:
    def __init__(self, app, secret_key):
        self.app = app
        self.security_layer = SecurityLayer(secret_key)

    def authenticate(self):
        """Middleware to authenticate incoming requests."""
        token = request.headers.get("Authorization")
        if not token or not self.security_layer.verify_signature("user", token):
            return jsonify({"status": "failed", "message": "Unauthorized"}), 401