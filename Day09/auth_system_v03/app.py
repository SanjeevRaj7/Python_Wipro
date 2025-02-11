from flask import Flask
from routes.auth import auth_bp
from utils.errors import APIError, handle_api_error

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')

# Register error handler
app.register_error_handler(APIError, handle_api_error)

if __name__ == "__main__":
    app.run(debug=True)
