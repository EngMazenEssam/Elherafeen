from flask import Blueprint, render_template, jsonify, request, abort
from models import DataRepository

shop_controller = Blueprint('shop', __name__)
repo = DataRepository()

@shop_controller.route('/')
def home():
    products = repo.get_all_products()
    categories = repo.get_categories()
    return render_template('index.html', products=products, categories=categories)

@shop_controller.route('/product/<product_id>')
def product_detail(product_id):
    product = repo.get_product_by_id(product_id)
    if not product:
        abort(404)
    return render_template('product_detail.html', product=product)

@shop_controller.route('/api/products')
def api_products():
    category = request.args.get('category')
    products = repo.get_all_products()
    if category and category != 'All':
        products = [p for p in products if p['category'] == category]
    return jsonify(products)