from werkzeug.security import generate_password_hash, check_password_hash
from config.database import get_db_connection

class User:
    @staticmethod
    def create_user(username, password, email):
        db = get_db_connection()
        cursor = db.cursor()
        password_hash = generate_password_hash(password)
        cursor.execute("""
            INSERT INTO users (username, password_hash, email)
            VALUES (%s, %s, %s)
        """, (username, password_hash, email))
        db.commit()
        db.close()

    @staticmethod
    def get_user_by_username(username):
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        db.close()
        return user
