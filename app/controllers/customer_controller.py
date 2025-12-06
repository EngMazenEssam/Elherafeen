from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session,
)
from app.services.user_service import UserService

customer_bp = Blueprint("customer", __name__)  # 👈 no url_prefix, so /login, /register
user_service = UserService()


@customer_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        fullname = request.form.get("fullname", "")
        email = request.form.get("email", "")
        phone = request.form.get("phone", "")
        password = request.form.get("password", "")
        confirm = request.form.get("confirm", "")

        try:
            user_service.register_user(
                fullname=fullname,
                email=email,
                phone=phone,
                password=password,
                confirm=confirm,
            )
            flash("Account created successfully! You can log in now.", "success")
            return redirect(url_for("customer.login"))
        except ValueError as e:
            flash(str(e), "error")
            return render_template("register.html")

    return render_template("register.html")


@customer_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "")
        password = request.form.get("password", "")

        try:
            user = user_service.login_user(email, password)

            # store user info in session
            session["user_id"] = user.id
            session["fullname"] = user.fullname
            session["email"] = user.email

            flash(f"Welcome back, {user.fullname}!", "success")
            return redirect(url_for("home.home"))
        except ValueError as e:
            flash(str(e), "error")
            return render_template("login.html")

    return render_template("login.html")
