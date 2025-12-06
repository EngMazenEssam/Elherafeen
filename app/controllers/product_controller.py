from flask import Blueprint, render_template, request, redirect, url_for, abort
from app.services.product_service import (
    get_product_by_id,
    get_categories,
    filter_products,
)
from app.services.cart_service import add_to_cart as cart_add_to_cart

product_bp = Blueprint("product", __name__)

@product_bp.get("/products")
def product_list():
    category = request.args.get("category", "All")
    search = request.args.get("search", "").strip()
    products = filter_products(
        category=None if category == "All" else category,
        search=search or None,
    )
    categories = get_categories()
    return render_template(
        "products.html",
        products=products,
        categories=categories,
        selected_category=category,
        search_term=search,
    )

@product_bp.get("/product/<product_id>")
def product_detail(product_id):
    product = get_product_by_id(product_id)
    if not product:
        abort(404)
    return render_template("product_detail.html", product=product)

@product_bp.post("/product/<product_id>/add-to-cart", endpoint="add_to_cart")
def add_to_cart_route(product_id):
    product = get_product_by_id(product_id)
    if not product:
        abort(404)
    quantity_str = request.form.get("quantity", "1")
    try:
        quantity = int(quantity_str)
    except ValueError:
        quantity = 1
    if quantity < 1:
        quantity = 1
    oem = product.get("oem")
    cart_add_to_cart(oem, quantity)
    return redirect(url_for("product.product_detail", product_id=product_id))
