from flask import Flask
from app.config import SECRET_KEY
from app.routes.customer_routes import customer_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = SECRET_KEY

    # تسجيل الـ blueprints
    app.register_blueprint(customer_bp)

    return app
