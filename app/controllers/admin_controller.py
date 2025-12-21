from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.services.admin_service import AdminService
from app.services.product_moderation_service import ProductModerationService

admin_bp = Blueprint("admin", __name__)

admin_service = AdminService()
moderation_service = ProductModerationService()


@admin_bp.route("/admin/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        try:
            admin = admin_service.login(email, password)
            session["admin_id"] = admin["id"]
            session["admin_name"] = admin["fullname"]
            return redirect(url_for("admin.dashboard"))
        except ValueError as e:
            flash(str(e), "error")

    return render_template("admin_login.html")


@admin_bp.route("/admin")
def dashboard():
    if "admin_id" not in session:
        return redirect(url_for("admin.login"))

    admin = {
        "name": session.get("admin_name", "Admin User"),
        "email": "admin@elherafeen.com",
    }

    requests = moderation_service.get_pending_products()

    return render_template(
        "admin.html",
        admin=admin,
        requests=requests
    )


@admin_bp.route("/admin/approve/<product_id>", methods=["POST"])
def approve(product_id):
    try:
        moderation_service.approve(product_id)
        flash("Product approved successfully", "success")
    except ValueError as e:
        flash(str(e), "error")

    return redirect(url_for("admin.dashboard"))


@admin_bp.route("/admin/reject/<product_id>", methods=["POST"])
def reject(product_id):
    try:
        moderation_service.reject(product_id)
        flash("Product rejected", "warning")
    except ValueError as e:
        flash(str(e), "error")

    return redirect(url_for("admin.dashboard"))
