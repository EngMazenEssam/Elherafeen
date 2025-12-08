from flask import Blueprint, render_template, request, redirect, url_for, flash
import json
from datetime import datetime
from pathlib import Path

checkout_bp = Blueprint('checkout', __name__)

def get_data_folder():
    base_dir = Path(__file__).parent.parent
    return base_dir / 'data'

def load_cart():
    cart_file = get_data_folder() / 'cart.json'
    try:
        with open(cart_file, 'r') as f:
            cart_data = json.load(f)
            if 'items' not in cart_data:
                cart_data['items'] = []
            if 'total_items' not in cart_data:
                cart_data['total_items'] = 0
            if 'total_price' not in cart_data:
                cart_data['total_price'] = 0
            return cart_data
    except FileNotFoundError:
        return {"items": [], "total_items": 0, "total_price": 0}

def load_products():
    products_file = get_data_folder() / 'sellers_inventory.json'
    try:
        with open(products_file, 'r', encoding='utf-8') as f:
            sellers = json.load(f)
            all_products = []
            for seller_id, seller_data in sellers.items():
                for product in seller_data['products']:
                    product['seller_name'] = seller_data['name']
                    product['id'] = f"{seller_id}_{product['oem']}"
                    all_products.append(product)
            return all_products
    except FileNotFoundError:
        return []

def save_orders(orders):
    orders_file = get_data_folder() / 'orders.json'
    with open(orders_file, 'w') as f:
        json.dump(orders, f, indent=2)

def clear_cart():
    cart_file = get_data_folder() / 'cart.json'
    empty_cart = {"items": [], "total_items": 0, "total_price": 0}
    with open(cart_file, 'w') as f:
        json.dump(empty_cart, f, indent=2)

@checkout_bp.route('/checkout')
def checkout_page():
    cart_data = load_cart()
    
    if not cart_data['items']:
        flash('Your cart is empty', 'error')
        return redirect('/cart')
    
    all_products = load_products()
    cart_items_with_details = []
    
    for cart_item in cart_data['items']:
        for product in all_products:
            if product['oem'] == cart_item['oem']:
                item_with_details = {
                    'name': product.get('name', 'Unknown Product'),
                    'oem': product.get('oem', ''),
                    'price': product.get('price', 0),
                    'quantity': cart_item['quantity'],
                    'brand': product.get('brand', ''),
                    'line_total': product.get('price', 0) * cart_item['quantity']
                }
                cart_items_with_details.append(item_with_details)
                break
    
    cart_data['items'] = cart_items_with_details
    
    return render_template('checkout.html', cart=cart_data)

@checkout_bp.route('/checkout', methods=['POST'])
def process_checkout():
    first_name = request.form.get('first_name', '').strip()
    last_name = request.form.get('last_name', '').strip()
    email = request.form.get('email', '').strip()
    phone = request.form.get('phone', '').strip()
    address = request.form.get('address', '').strip()
    city = request.form.get('city', '').strip()
    zip_code = request.form.get('zip', '').strip()
    payment_method = request.form.get('payment', 'cod')
    
    if not all([first_name, last_name, email, phone, address, city, zip_code]):
        flash('Please fill in all required fields', 'error')
        return redirect('/checkout')
    
    cart_data = load_cart()
    
    if not cart_data['items']:
        flash('Your cart is empty', 'error')
        return redirect('/cart')
    
    order_id = f"ORD-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    all_products = load_products()
    order_items = []
    
    for cart_item in cart_data['items']:
        for product in all_products:
            if product['oem'] == cart_item['oem']:
                order_item = {
                    'name': product.get('name', 'Unknown Product'),
                    'oem': product.get('oem', ''),
                    'price': product.get('price', 0),
                    'quantity': cart_item['quantity'],
                    'brand': product.get('brand', ''),
                    'category': product.get('category', ''),
                    'line_total': product.get('price', 0) * cart_item['quantity']
                }
                order_items.append(order_item)
                break
    
    order = {
        'order_id': order_id,
        'customer': {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone': phone,
            'address': address,
            'city': city,
            'zip_code': zip_code
        },
        'items': order_items,
        'total_items': cart_data['total_items'],
        'total_price': cart_data['total_price'],
        'payment_method': payment_method,
        'status': 'pending',
        'order_date': datetime.now().isoformat(),
        'notes': ''
    }
    
    try:
        with open(get_data_folder() / 'orders.json', 'r') as f:
            orders = json.load(f)
    except FileNotFoundError:
        orders = []
    
    orders.append(order)
    
    with open(get_data_folder() / 'orders.json', 'w') as f:
        json.dump(orders, f, indent=2)
    
    clear_cart()
    
    return redirect(f'/order-confirmation/{order_id}')

@checkout_bp.route('/order-confirmation/<order_id>')
def order_confirmation(order_id):
    try:
        with open(get_data_folder() / 'orders.json', 'r') as f:
            orders = json.load(f)
        
        order = None
        for o in orders:
            if o['order_id'] == order_id:
                order = o
                break
        
        if not order:
            flash('Order not found', 'error')
            return redirect('/')
        
        return render_template('order_confirmation.html', order=order)
    
    except FileNotFoundError:
        flash('Order not found', 'error')
        return redirect('/')

@checkout_bp.route('/orders')
def order_history():
    try:
        with open(get_data_folder() / 'orders.json', 'r') as f:
            orders = json.load(f)
        
        orders.sort(key=lambda x: x.get('order_date', ''), reverse=True)
        
        return render_template('order_history.html', orders=orders)
    
    except FileNotFoundError:
        return render_template('order_history.html', orders=[])