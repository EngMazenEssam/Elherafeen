from flask import Flask
from app.config import SECRET_KEY
from app.routes.customer_routes import customer_bp

app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = SECRET_KEY

# تسجيل الـ blueprints
app.register_blueprint(customer_bp)

if __name__ == "__main__":
    app.run(debug=True)
