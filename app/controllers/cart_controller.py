from flask import Blueprint, render_template, request, jsonify
from app.services.cart_service import (
    get_cart_items_with_totals,
    update_cart_quantity,
    remove_from_cart,
)

cart_bp = Blueprint("cart", __name__)


@cart_bp.get("/cart", endpoint="cart")
def cart_page():
    """Render the cart page."""
    cart_items, subtotal, total_quantity = get_cart_items_with_totals()

    shipping = 100
    tax = round(subtotal * 0.14, 2)
    total = subtotal + shipping + tax
    currency = "EGP"

    return render_template(
        "cart.html",
        cart_items=cart_items,
        subtotal=subtotal,
        shipping=shipping,
        tax=tax,
        total=total,
        total_quantity=total_quantity,
        currency=currency
    )


@cart_bp.post("/cart/update-quantity", endpoint="update_cart_quantity")
def update_cart_quantity_route():
    data = request.get_json(silent=True) or {}
    oem = data.get("oem")
    quantity = data.get("quantity")

    if not oem:
        return jsonify({"ok": False, "error": "Missing OEM"}), 400

    try:
        quantity = int(quantity)
    except (TypeError, ValueError):
        return jsonify({"ok": False, "error": "Invalid quantity"}), 400

    if quantity < 1:
        quantity = 1

    ok, error, status = update_cart_quantity(oem, quantity)
    if not ok:
        return jsonify({"ok": False, "error": error}), status

    return jsonify({"ok": True}), 200


@cart_bp.post("/cart/remove", endpoint="remove_from_cart")
def remove_from_cart_route():
    data = request.get_json(silent=True) or {}
    oem = data.get("oem")

    if not oem:
        return jsonify({"ok": False, "error": "Missing OEM"}), 400

    ok, error, status = remove_from_cart(oem)
    if not ok:
        return jsonify({"ok": False, "error": error}), status

    return jsonify({"ok": True}), 200
