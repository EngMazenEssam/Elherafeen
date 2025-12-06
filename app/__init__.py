from flask import Flask

def create_app():
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static",
    )

    from app.controllers.home_controller import home_bp
    from app.controllers.cart_controller import cart_bp
    from app.controllers.product_controller import product_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(product_bp)

    return app
