from flask import Blueprint, render_template, request, abort, redirect, url_for, session
from models import DataRepository

shop_controller = Blueprint('shop', __name__)
repo = DataRepository()

@shop_controller.route('/')
def home():
    category = request.args.get('category', 'All')
    search = request.args.get('search', '')
    
    products = repo.get_products_filtered(category=category if category != 'All' else None, search=search)
    categories = repo.get_categories()
    
    return render_template('index.html', 
                         products=products, 
                         categories=categories,
                         selected_category=category,
                         search_term=search)

@shop_controller.route('/product/<product_id>')
def product_detail(product_id):
    product = repo.get_product_by_id(product_id)
    if not product:
        abort(404)
    return render_template('product_detail.html', product=product)

@shop_controller.route('/search', methods=['GET', 'POST'])
def search():
    search_term = request.args.get('q', '') or request.form.get('search', '')
    products = repo.search_products(search_term) if search_term else []
    categories = repo.get_categories()
    
    return render_template('index.html',
                         products=products,
                         categories=categories,
                         search_term=search_term,
                         selected_category='All')

@shop_controller.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    product_id = request.form.get('product_id')
    quantity = request.form.get('quantity', '1')
    
    if 'cart' not in session:
        session['cart'] = []
    
    # Add product to cart
    session['cart'].append({
        'product_id': product_id,
        'quantity': int(quantity)
    })
    session.modified = True
    
    # Redirect back to product detail
    return redirect(url_for('shop.product_detail', product_id=product_id))