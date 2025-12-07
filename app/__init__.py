from flask import Flask
import os


def create_app():
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static",
    )

    app.config["SECRET_KEY"] = os.environ.get(
        "SECRET_KEY", "dev-secret-change-me"
    )

    from app.controllers.home_controller import home_bp
    from app.controllers.cart_controller import cart_bp
    from app.controllers.product_controller import product_bp
    from app.controllers.customer_controller import customer_bp
    from app.controllers.checkout_controller import checkout_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(customer_bp)
    app.register_blueprint(checkout_bp)

    return app
