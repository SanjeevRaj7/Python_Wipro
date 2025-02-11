from flask import Blueprint, request, jsonify
from models.user import User
from models.token import Token
from utils.logger import log_request, log_error
from utils.errors import APIError
from werkzeug.security import check_password_hash
from datetime import datetime, timedelta
from config.settings import SECRET_KEY
import jwt

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        username = data.get("username")
        password = data.get("password")
        email = data.get("email")

        if not username or not password or not email:
            raise APIError("Missing required fields", 400)

        User.create_user(username, password, email)
        log_request('/register', 'POST', data, 201)
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        log_error(str(e))
        raise APIError("Failed to register user", 500)

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get("username")
        password = data.get("password")

        user = User.get_user_by_username(username)
        if user and user["password_hash"] and check_password_hash(user["password_hash"], password):
            access_token = Token.generate_access_token(user["id"])
            refresh_token = Token.generate_refresh_token(user["id"])
            expires_at = datetime.utcnow() + timedelta(hours=1)

            Token.save_token(user["id"], access_token, expires_at)
            log_request('/login', 'POST', data, 200)
            return jsonify({
                "access_token": access_token,
                "refresh_token": refresh_token
            }), 200

        log_request('/login', 'POST', data, 401)
        raise APIError("Invalid credentials", 401)
    except Exception as e:
        log_error(str(e))
        raise APIError("Failed to login", 500)

@auth_bp.route('/validate', methods=['GET'])
def validate_token():
    try:
        # log_request('/validate', 'GET', request, 401)
        log_request('/validate','GET',request.json, 200)

        # Get the token from the Authorization header
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith("Bearer "):
            raise APIError("Missing or invalid token", 401)

        token = auth_header.split(" ")[1]

        # Decode the JWT token
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_id = payload.get('user_id')

        return jsonify({"message": f"Token is valid. User ID: {user_id}"}), 200

    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Access token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid access token"}), 401
    except Exception as e:
        log_error(e)
        return jsonify({"error": "An error occurred"}), 500
