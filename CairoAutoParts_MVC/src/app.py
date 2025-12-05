from flask import Flask
from controllers import Products

app = Flask(__name__)
app.register_blueprint(Products)

if __name__ == '__main__':
    app.run(debug=True)