from flask import Flask

def create_app():
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static",
    )

    from app.controllers.cart_controller import cart_bp
    app.register_blueprint(cart_bp)

    return app
