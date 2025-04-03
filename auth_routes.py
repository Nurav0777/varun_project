from flask import Blueprint, request, jsonify
from services.auth_service import AuthService

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    return AuthService.register(data["username"], data["password"])

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    return AuthService.login(data["username"], data["password"])
