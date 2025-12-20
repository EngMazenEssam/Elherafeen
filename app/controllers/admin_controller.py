from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.services.admin_service import AdminService

admin_bp = Blueprint("admin", __name__)
service = AdminService()


@admin_bp.route("/admin/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        try:
            admin = service.login(email, password)
            session["admin_id"] = admin["id"]
            session["admin_name"] = admin["fullname"]
            return redirect(url_for("admin.dashboard"))
        except ValueError as e:
            flash(str(e), "error")

    return render_template("admin_login.html")


@admin_bp.route("/admin")
def dashboard():
    admin = {
        "name": session.get("admin_name", "Admin User"),
        "email": "admin@elherafeen.com",
    }
    requests = []  # مؤقت لحد ما نربطه بالـ JSON

    return render_template(
        "admin.html",
        admin=admin,
        requests=requests
    )

