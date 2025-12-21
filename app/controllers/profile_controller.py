from flask import Blueprint, render_template, request, redirect, url_for
import app.services.user_service as us

from app.services.address_service import AddressService
from app.services.user_service import UserService
from app.services.order_service import get_orders_for_user
from app.services.address_service import AddressService


profile_bp = Blueprint(
    "profile",
    __name__,
    url_prefix="/profile"
)

@profile_bp.route("/")
def profile():
    email = "mazenessam@gmail.com"

    user_service = UserService()
    user = user_service.repo.find_by_email(email)

    if not user:
        return "User not found", 404

    orders = get_orders_for_user(email)
    address_service = AddressService()
    address = address_service.get_address_for_user(email)


    return render_template(
        "profile.html",
        user=user,
        orders=orders,
        address=address
    )

@profile_bp.route('/profile/edit', methods=['GET'])
def edit_profile_page():
    email = "mazenessam@gmail.com"

    user_service = UserService()
    user = user_service.repo.find_by_email(email)

    if not user:
        return "User not found", 404

    return render_template("edit_profile.html", user=user)



@profile_bp.route('/profile/edit', methods=['POST'])
def edit_profile():
    email = "mazenessam@gmail.com"

    fullname = request.form.get("fullname")
    phone = request.form.get("phone")

    user_service = UserService()

    updated = user_service.update_user(
        email=email,
        fullname=fullname,
        phone=phone
    )

    if not updated:
        return "Update failed", 400

    return redirect(url_for("profile.profile"))

print(us.__file__)


@profile_bp.route("/address/edit", methods=["GET"])
def edit_address_page():
    email = "mazenessam@gmail.com"

    address_service = AddressService()
    address = address_service.get_address_for_user(email)

    if not address:
        return "Address not found", 404

    return render_template("edit_address.html", address=address)


@profile_bp.route("/address/edit", methods=["POST"])
def edit_address():
    email = "mazenessam@gmail.com"

    street = request.form.get("street")
    city = request.form.get("city")
    country = request.form.get("country")
    phone = request.form.get("phone")

    address_service = AddressService()
    updated = address_service.update_address(
        email=email,
        street=street,
        city=city,
        country=country,
        phone=phone
    )

    if not updated:
        return "Update failed", 400

    return redirect(url_for("profile.profile"))
