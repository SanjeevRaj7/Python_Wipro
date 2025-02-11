from config.database import get_db_connection
from flask import Flask
from routes.auth import auth_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == "__main__":
    app.run(debug=True)
