from flask import Blueprint, render_template, request, redirect, url_for, flash
import json
from datetime import datetime

from app.services.cart_service import get_cart_items_with_totals
from app.repository.checkout_repository import (
    get_data_folder,
    save_orders,
    clear_cart,
)

checkout_bp = Blueprint("checkout", __name__)


@checkout_bp.route("/checkout")
def checkout_page():
    cart_items, subtotal, total_quantity = get_cart_items_with_totals()

    if total_quantity == 0:
        flash("Your cart is empty", "error")
        return redirect(url_for("cart.cart"))

    shipping = 100
    tax = round(subtotal * 0.14, 2)
    grand_total = subtotal + shipping + tax

    checkout_items = []
    for item in cart_items:
        product = item["product"]

        name = product.get("name", "Unknown product")
        oem = product.get("oem")
        price = product.get("price", 0)
        quantity = item.get("quantity", 1)
        brand = product.get("brand", "")
        line_total = item.get("line_total", 0)

        checkout_item = {
            "name": name,
            "oem": oem,
            "price": price,
            "quantity": quantity,
            "brand": brand,
            "line_total": line_total,
        }

        checkout_items.append(checkout_item)

    cart_view = {
        "items": checkout_items,
        "total_items": total_quantity,
        "subtotal": subtotal,
        "shipping": shipping,
        "tax": tax,
        "total_price": grand_total,
    }

    return render_template(
        "checkout.html",
        cart=cart_view,
        cart_items=checkout_items,
    )


@checkout_bp.route("/checkout", methods=["POST"])
def process_checkout():
    first_name = request.form.get("first_name", "").strip()
    last_name = request.form.get("last_name", "").strip()
    email = request.form.get("email", "").strip()
    phone = request.form.get("phone", "").strip()
    address = request.form.get("address", "").strip()
    city = request.form.get("city", "").strip()
    zip_code = request.form.get("zip", "").strip()
    payment_method = request.form.get("payment", "cod")

    if (
        first_name == "" or
        last_name == "" or
        email == "" or
        phone == "" or
        address == "" or
        city == "" or
        zip_code == ""
    ):
        flash("Please fill in all required fields", "error")
        return redirect(url_for("checkout.checkout_page"))

    cart_items, subtotal, total_quantity = get_cart_items_with_totals()

    if total_quantity == 0:
        flash("Your cart is empty", "error")
        return redirect(url_for("cart.cart"))

    shipping = 100
    tax = round(subtotal * 0.14, 2)
    grand_total = subtotal + shipping + tax

    order_items = []
    for item in cart_items:
        product = item["product"]

        name = product.get("name", "Unknown product")
        oem = product.get("oem")
        price = product.get("price", 0)
        quantity = item.get("quantity", 1)
        brand = product.get("brand", "")
        category = product.get("category", "")
        line_total = item.get("line_total", 0)

        order_item = {
            "name": name,
            "oem": oem,
            "price": price,
            "quantity": quantity,
            "brand": brand,
            "category": category,
            "line_total": line_total,
        }

        order_items.append(order_item)

    now = datetime.now()
    order_id_part = now.strftime("%Y%m%d%H%M%S")
    order_id = "ORD-" + order_id_part

    order = {
        "order_id": order_id,
        "customer": {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "address": address,
            "city": city,
            "zip_code": zip_code,
        },
        "items": order_items,
        "total_items": total_quantity,
        "subtotal": subtotal,
        "shipping": shipping,
        "tax": tax,
        "total_price": grand_total,
        "payment_method": payment_method,
        "status": "pending",
        "order_date": datetime.now().isoformat(),
        "notes": "",
    }

    orders_file_path = get_data_folder() / "orders.json"
    try:
        with open(orders_file_path, "r", encoding="utf-8") as f:
            orders = json.load(f)
    except FileNotFoundError:
        orders = []

    orders.append(order)
    save_orders(orders)

    clear_cart()

    return redirect(url_for("checkout.order_confirmation", order_id=order_id))


@checkout_bp.route("/order-confirmation/<order_id>")
def order_confirmation(order_id):
    orders_file_path = get_data_folder() / "orders.json"

    try:
        with open(orders_file_path, "r", encoding="utf-8") as f:
            orders = json.load(f)

        order = None
        for single_order in orders:
            if single_order.get("order_id") == order_id:
                order = single_order
                break

        if order is None:
            flash("Order not found", "error")
            return redirect(url_for("home.home"))

        return render_template("order_confirmation.html", order=order)

    except FileNotFoundError:
        flash("Order not found", "error")
        return redirect(url_for("home.home"))


@checkout_bp.route("/orders")
def order_history():
    orders_file_path = get_data_folder() / "orders.json"

    try:
        with open(orders_file_path, "r", encoding="utf-8") as f:
            orders = json.load(f)

        def get_order_date(order):
            return order.get("order_date", "")

        orders.sort(key=get_order_date, reverse=True)

        return render_template("order_history.html", orders=orders)

    except FileNotFoundError:
        return render_template("order_history.html", orders=[])
