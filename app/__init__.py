from flask import Flask
from app.config import SECRET_KEY

def create_app() -> Flask:
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.secret_key = SECRET_KEY

    # تسجيل الـ blueprints
    app.register_blueprint(customer_bp)

    return app
