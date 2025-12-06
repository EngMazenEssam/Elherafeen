from flask import Flask
from app.config import SECRET_KEY
from app.routes.customer_routes import customer_bp
from app import create_app


from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
