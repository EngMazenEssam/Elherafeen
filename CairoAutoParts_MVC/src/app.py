from flask import Flask
from controllers import shop_controller

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'
app.register_blueprint(shop_controller)

if __name__ == '__main__':
    app.run(debug=True)