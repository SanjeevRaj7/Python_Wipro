from flask import Blueprint, request, jsonify
from ..models.user import User
from ..models.token import Token
from datetime import datetime, timedelta

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")

    if not username or not password or not email:
        return jsonify({"error": "Missing required fields"}), 400

    User.create_user(username, password, email)
    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = User.get_user_by_username(username)
    if user and user["password_hash"] and check_password_hash(user["password_hash"], password):
        access_token = Token.generate_access_token(user["id"])
        refresh_token = Token.generate_refresh_token(user["id"])
        expires_at = datetime.utcnow() + timedelta(hours=1)

        Token.save_token(user["id"], access_token, expires_at)

        return jsonify({
            "access_token": access_token,
            "refresh_token": refresh_token
        }), 200
    return jsonify({"error": "Invalid credentials"}), 401

@auth_bp.route('/validate', methods=['POST'])
def validate():
    data = request.json
    access_token = data.get("access_token")

    user_id = Token.validate_token(access_token)
    if user_id:
        return jsonify({"message": "Token is valid", "user_id": user_id}), 200
    return jsonify({"error": "Invalid or expired token"}), 401
