from flask import Flask
from controllers import shop_controller

app = Flask(__name__)
app.register_blueprint(shop_controller)

if __name__ == '__main__':
    app.run(debug=True)