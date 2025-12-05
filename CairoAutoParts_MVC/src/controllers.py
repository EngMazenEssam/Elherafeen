from flask import Blueprint, render_template, jsonify, request, abort
from models import DataRepository

Products = Blueprint('shop', __name__)
repo = DataRepository()

@Products.route('/')
def home():
    products = repo.get_all_products()
    categories = repo.get_categories()
    return render_template('index.html', products=products, categories=categories)

@Products.route('/product/<product_id>')
def product_detail(product_id):
    product = repo.get_product_by_id(product_id)
    return render_template('product_detail.html', product=product)

