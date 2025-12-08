from flask import Blueprint, render_template, request, jsonify
from app.services.cart_service import (
    get_cart_items_with_totals,
    update_cart_quantity,
    remove_from_cart,
    add_to_cart,
)

cart_bp = Blueprint("cart", __name__)


@cart_bp.get("/cart", endpoint="cart")
def cart_page():

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
        currency=currency,
    )


@cart_bp.post("/cart/update-quantity", endpoint="update_cart_quantity")
def update_cart_quantity_route():

    data = request.get_json(silent=True) or {}

    oem = data.get("oem")
    quantity = data.get("quantity")

    if quantity < 1:
        quantity = 1

    ok, error, status = update_cart_quantity(oem, quantity)

    return jsonify({"ok": True}), 200


@cart_bp.post("/cart/remove", endpoint="remove_from_cart")
def remove_from_cart_route():

    data = request.get_json(silent=True) or {}
    oem = data.get("oem")

    ok, error, status = remove_from_cart(oem)

    if not ok:
        return jsonify({"ok": False, "error": error}), status

    return jsonify({"ok": True}), 200


@cart_bp.post("/cart/add", endpoint="add_to_cart")
def add_to_cart_route():

    data = request.get_json(silent=True) or {}

    oem = data.get("oem")
    quantity = data.get("quantity", 1)

    ok, error, status = add_to_cart(oem, quantity)

    if not ok:
        return jsonify({"ok": False, "error": error}), status

    return jsonify({"ok": True}), 200