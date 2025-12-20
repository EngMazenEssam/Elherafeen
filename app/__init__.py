import os
from flask import Flask

from app.controllers.home_controller import home_bp
from app.controllers.cart_controller import cart_bp
from app.controllers.product_controller import product_bp
from app.controllers.customer_controller import customer_bp
from app.controllers.checkout_controller import checkout_bp
from app.controllers.profile_controller import profile_bp
from app.controllers.marketplace_controller import marketplace_bp
from app.controllers.seller_controller import seller_bp


def create_app():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    app = Flask(
        __name__,
        template_folder=os.path.join(BASE_DIR, "app", "templates"),
        static_folder=os.path.join(BASE_DIR, "app", "static")
    )

    app.config["SECRET_KEY"] = os.environ.get(
        "SECRET_KEY", "dev-secret-change-me"
    )

    app.register_blueprint(home_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(customer_bp)
    app.register_blueprint(checkout_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(marketplace_bp)
    app.register_blueprint(seller_bp)

    return app
