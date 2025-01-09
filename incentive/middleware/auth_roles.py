import jwt
from functools import wraps
from flask import request, jsonify

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

class RoleManager:
    def __init__(self):
        """Initialize the role manager."""
        self.roles = {
            "admin": ["create", "delete", "update", "read"],
            "user": ["read"]
        }

    def check_permission(self, role, permission):
        """Check if a role has the required permission."""
        return permission in self.roles.get(role, [])

def token_required(f):
    """Decorator to check JWT token in headers."""
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"status": "failed", "message": "Token is missing"}), 403
        try:
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            request.user = decoded_token["user"]
        except jwt.ExpiredSignatureError:
            return jsonify({"status": "failed", "message": "Token has expired"}), 403
        except jwt.InvalidTokenError:
            return jsonify({"status": "failed", "message": "Invalid token"}), 403
        return f(*args, **kwargs)
    return decorator

def role_required(permission):
    """Decorator to check role-based permissions."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user_role = request.user.get("role", "user")
            if not RoleManager().check_permission(user_role, permission):
                return jsonify({"status": "failed", "message": "Permission denied"}), 403
            return func(*args, **kwargs)
        return wrapper
    return decorator