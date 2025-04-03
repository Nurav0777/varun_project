from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

def jwt_required_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
            return func(*args, **kwargs)
        except Exception as e:
            return jsonify({"error": "Unauthorized", "message": str(e)}), 401
    return wrapper
