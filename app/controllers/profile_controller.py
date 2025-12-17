from flask import Blueprint, render_template
from app.services.user_service import UserService
from app.services.order_service import get_orders_for_user
from app.services.address_service import get_address_for_user

profile_bp = Blueprint(
    "profile",
    __name__,
    url_prefix="/profile"
)

@profile_bp.route("/")
def profile():
    # TEMP until auth/session is added
    email = "mazenessam@gmail.com"

    user_service = UserService()
    user = user_service.repo.find_by_email(email)

    if not user:
        return "User not found", 404

    orders = get_orders_for_user(email)
    address = get_address_for_user(email)

    return render_template(
        "profile.html",
        user=user,
        orders=orders,
        address=address
    )
