from flask import Blueprint, render_template

home_bp = Blueprint("home", __name__)


@home_bp.get("/")
def home():
    """Main landing page: /"""
    return render_template("home.html")
