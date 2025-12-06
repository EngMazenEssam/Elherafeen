from flask import Blueprint, render_template, request, redirect, url_for
from models import DataRepository

Products_controller = Blueprint('shop', __name__)
repo = DataRepository()

@Products_controller.route('/')
def home():
    category = request.args.get('category', 'All')
    search = request.args.get('search', '')
    
    category_filter = None
    if category != 'All':
        category_filter = category
    
    products = repo.get_products_filtered(category=category_filter, search=search)
    categories = repo.get_categories()
    return render_template('index.html', products=products, categories=categories,selected_category=category,search_term=search)

@Products_controller.route('/product/<product_id>')
def product_detail(product_id):
    product = repo.get_product_by_id(product_id)
    return render_template('product_detail.html', product=product)

@Products_controller.route('/search', methods=['GET', 'POST'])
def search():
    search_term = ''
    
    if request.args.get('q'):
        search_term = request.args.get('q')
    elif request.form.get('search'):
        search_term = request.form.get('search')
    
    products = []
    if search_term:
        products = repo.search_products(search_term)
    categories = repo.get_categories()
    
    return render_template('index.html',products=products,categories=categories,search_term=search_term,selected_category='All')

@Products_controller.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    product_id = request.form.get('product_id')
    quantity_str = request.form.get('quantity', '1')
    
    try:
        quantity = int(quantity_str)
    except:
        quantity = 1
    
    product = repo.get_product_by_id(product_id)
    cart = repo.load_cart()
    product_oem = product['oem']
    
    found_item = None
    for item in cart['items']:
        if item['oem'] == product_oem:
            found_item = item
            break
    
    if found_item:
        found_item['quantity'] = found_item['quantity'] + quantity
    else:
        new_item = {
            'oem': product_oem,
            'quantity': quantity
        }
        cart['items'].append(new_item)
    
    repo.save_cart(cart)
    
    return redirect(url_for('shop.product_detail', product_id=product_id))

@Products_controller.route('/update-cart', methods=['POST'])
def update_cart():
    product_id = request.form.get('product_id')
    action = request.form.get('action')
    
    product = repo.get_product_by_id(product_id)
    cart = repo.load_cart()
    product_oem = product['oem']
    
    found_item = None
    for item in cart['items']:
        if item['oem'] == product_oem:
            found_item = item
            break
    
    if found_item:
        if action == 'increase':
            found_item['quantity'] = found_item['quantity'] + 1
        elif action == 'decrease':
            found_item['quantity'] = found_item['quantity'] - 1
            
            if found_item['quantity'] <= 0:
                cart['items'].remove(found_item)
        
        repo.save_cart(cart)
    
    return redirect(url_for('shop.cart'))

@Products_controller.route('/remove-from-cart', methods=['POST'])
def remove_from_cart():
    product_id = request.form.get('product_id')
    product = repo.get_product_by_id(product_id)
    cart = repo.load_cart()
    product_oem = product['oem']
    
    new_items = []
    for item in cart['items']:
        if item['oem'] != product_oem:
            new_items.append(item)
    
    cart['items'] = new_items
    repo.save_cart(cart)
    
    return redirect(url_for('shop.cart'))

@Products_controller.route('/cart')
def cart():
    items = repo.get_cart_items()
    total_items, total_price = repo.get_cart_total()
    
    cart_data = {
        'items': items,
        'total_items': total_items,
        'total_price': total_price
    }
    
    return render_template('cart.html', cart=cart_data)