import jwt
from functools import wraps
from flask import request, jsonify, current_app


def auth_required(roles=None):
    """
    Decorator to check for a valid JWT and optionally restrict access by role.
    Usage: @auth_required(roles=['admin']) or @auth_required()
    """

    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.headers.get('Authorization')
            if not token:
                return jsonify({"message": "Token is missing!"}), 401

            # The token is expected in the format "Bearer <token>"
            if "Bearer " in token:
                token = token.split(" ")[1]

            try:
                data = jwt.decode(token, current_app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
                current_user = data
            except jwt.ExpiredSignatureError:
                return jsonify({"message": "Token has expired!"}), 401
            except jwt.InvalidTokenError:
                return jsonify({"message": "Token is invalid!"}), 401

            if roles and current_user['role'] not in roles:
                return jsonify({"message": "Access denied: insufficient permissions."}), 403

            return f(current_user, *args, **kwargs)

        return decorated

    return decorator
