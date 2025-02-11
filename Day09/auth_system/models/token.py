#this file manages token related database operation

from datetime import datetime, timedelta
from pythonia.day09.auth_system.config.database import get_db_connection
from pythonia.day09.auth_system.config.settings import SECRET_KEY

import jwt

class Token:
    @staticmethod
    def generate_access_token(user_id):

        payload = {
            "user_id":user_id,
            "exp": datetime.utcnow() + timedelta(hours=1)
        }
        return jwt.encode(payload, SECRET_KEY, algorithm='HS256')


    @staticmethod
    def generate_refresh_token(user_id):
        payload = {
            "user_id":user_id,
            "exp": datetime.utcnow() + timedelta(days=30)
        }
        return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    @staticmethod
    def save_token(user_id,access_token,expires_at):
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("""
        INSERT INTO token (user_id, access_token, expires_at)
        VALUES (%s, %s, %s)""", (user_id, access_token, expires_at))

        db.commit()
        db.close()

    @staticmethod
    def validate_token(access_token):
        try:
            decoded = jwt.decode(access_token, SECRET_KEY, algorithms=['HS256'])
            return decoded["user_id"]
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
