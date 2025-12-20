from flask import Blueprint, render_template, request
from app.services.marketplace_service import (
    get_all_products,
    get_product_by_id,
    filter_products
)

marketplace_bp = Blueprint(
    "marketplace",
    __name__,
    url_prefix="/marketplace"
)


@marketplace_bp.route("/")
def list_products():
    category = request.args.get("category")
    search = request.args.get("search")

    products = filter_products(category=category, search=search)

    return render_template(
        "products.html",
        products=products
    )


@marketplace_bp.route("/<product_id>")
def product_detail(product_id):
    product = get_product_by_id(product_id)
    if not product:
        return "Product not found", 404

    return render_template(
        "product_detail.html",
        product=product
    )
