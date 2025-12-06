import json
from pathlib import Path

# --- CONFIGURATION ---
PROJECT_ROOT = Path("CairoAutoParts_MVC")

# --- JSON DATA ---
sellers_inventory = {
  "SELLER_01": {
    "name": "Cairo Auto Parts", "phone": "+20 123 456 7890", "location": "Nasr City, Cairo", "rating": 4.8,
    "products": [
      {"oem": "152566", "name": "Mobil 1 FS x1 5W-40 Synthetic Oil", "category": "Fluids", "type": "Oil", "brand": "Mobil 1", "condition": "New", "price": 850, "currency": "EGP", "stock": 50, "images": ["placeholder"], "description": "Advanced full synthetic engine oil.", "sold_count": 120, "tags": ["oil", "maintenance"]},
      {"oem": "09.A448.11", "name": "Brembo Coated Disc Brake Rotor", "category": "Brakes", "type": "Rotor", "brand": "Brembo", "condition": "New", "price": 2400, "currency": "EGP", "stock": 10, "images": ["placeholder"], "description": "High carbon UV coated disc.", "sold_count": 55, "tags": ["brakes", "performance"]},
      {"oem": "574012068", "name": "Varta Silver Dynamic E11 Battery", "category": "Electrical", "type": "Battery", "brand": "Varta", "condition": "New", "price": 3500, "currency": "EGP", "stock": 8, "images": ["placeholder"], "description": "74Ah 680A Heavy duty battery.", "sold_count": 10, "tags": ["power", "battery"]},
      {"oem": "339031", "name": "KYB Excel-G Gas Strut (Front Right)", "category": "Suspension", "type": "Strut", "brand": "KYB", "condition": "New", "price": 2100, "currency": "EGP", "stock": 20, "images": ["placeholder"], "description": "Twin-tube gas shock absorber.", "sold_count": 32, "tags": ["suspension", "shock"]},
      {"oem": "KP15680XS", "name": "Gates Water Pump Kit", "category": "Cooling", "type": "Pump", "brand": "Gates", "condition": "New", "price": 1850, "currency": "EGP", "stock": 5, "images": ["placeholder"], "description": "Includes timing belt and water pump.", "sold_count": 14, "tags": ["cooling", "timing"]},
      {"oem": "64210", "name": "Osram Night Breaker H7", "category": "Electrical", "type": "Lighting", "brand": "Osram", "condition": "New", "price": 450, "currency": "EGP", "stock": 100, "images": ["placeholder"], "description": "Up to 150% more brightness.", "sold_count": 300, "tags": ["light", "safety"]}
    ]
  },
  "SELLER_02": {
    "name": "Alexandria Spares Hub", "phone": "+20 100 987 6543", "location": "Smouha, Alexandria", "rating": 4.5,
    "products": [
      {"oem": "0986494019", "name": "Bosch Disc Brake Pads", "category": "Brakes", "type": "Pads", "brand": "Bosch", "condition": "New", "price": 1150, "currency": "EGP", "stock": 25, "images": ["placeholder"], "description": "QuietCast Premium Disc Brake Pads.", "sold_count": 88, "tags": ["brakes", "deal"]},
      {"oem": "221-3600", "name": "Denso Radiator Assembly", "category": "Cooling", "type": "Radiator", "brand": "Denso", "condition": "New", "price": 4200, "currency": "EGP", "stock": 4, "images": ["placeholder"], "description": "OEM fit plastic tank aluminum core.", "sold_count": 2, "tags": ["cooling", "radiator"]},
      {"oem": "SILZKGR8B8S", "name": "NGK Laser Iridium Spark Plug", "category": "Engine", "type": "Ignition", "brand": "NGK", "condition": "New", "price": 900, "currency": "EGP", "stock": 100, "images": ["placeholder"], "description": "Long life iridium plug (Pack of 4).", "sold_count": 200, "tags": ["ignition", "spark plug"]},
      {"oem": "15D5B8", "name": "Castrol React DOT 4 Brake Fluid", "category": "Fluids", "type": "Hydraulic", "brand": "Castrol", "condition": "New", "price": 150, "currency": "EGP", "stock": 60, "images": ["placeholder"], "description": "High performance synthetic brake fluid.", "sold_count": 40, "tags": ["safety", "fluids"]},
      {"oem": "2991601", "name": "Lemförder Control Arm", "category": "Suspension", "type": "Control Arm", "brand": "Lemförder", "condition": "New", "price": 3100, "currency": "EGP", "stock": 6, "images": ["placeholder"], "description": "Front axle, left, with bushings.", "sold_count": 3, "tags": ["suspension", "german"]},
      {"oem": "941006", "name": "Dayco Timing Belt", "category": "Engine", "type": "Belt", "brand": "Dayco", "condition": "New", "price": 600, "currency": "EGP", "stock": 40, "images": ["placeholder"], "description": "High tenacity timing belt.", "sold_count": 60, "tags": ["engine", "belt"]}
    ]
  },
  "SELLER_03": {
    "name": "Giza Performance", "phone": "+20 111 222 3344", "location": "Dokki, Giza", "rating": 4.9,
    "products": [
      {"oem": "376045SP", "name": "Monroe OESpectrum Rear Shock", "category": "Suspension", "type": "Shock", "brand": "Monroe", "condition": "New", "price": 1350, "currency": "EGP", "stock": 14, "images": ["placeholder"], "description": "Rear shock absorber for smooth ride.", "sold_count": 22, "tags": ["suspension", "rear"]},
      {"oem": "W712/95", "name": "Mann-Filter Oil Filter", "category": "Engine", "type": "Filter", "brand": "Mann", "condition": "New", "price": 250, "currency": "EGP", "stock": 30, "images": ["placeholder"], "description": "Spin-on oil filter with anti-drain valve.", "sold_count": 95, "tags": ["filter", "maintenance"]},
      {"oem": "439864", "name": "Valeo Alternator 14V", "category": "Electrical", "type": "Charging", "brand": "Valeo", "condition": "Used", "price": 1800, "currency": "EGP", "stock": 1, "images": ["placeholder"], "description": "Refurbished unit, tested output.", "sold_count": 1, "tags": ["charging", "used"]},
      {"oem": "550046646", "name": "Shell Helix Ultra 5W-30", "category": "Fluids", "type": "Oil", "brand": "Shell", "condition": "New", "price": 950, "currency": "EGP", "stock": 45, "images": ["placeholder"], "description": "Fully synthetic motor oil 4L.", "sold_count": 210, "tags": ["oil", "engine"]},
      {"oem": "TX1887D", "name": "Mahle Thermostat", "category": "Cooling", "type": "Thermostat", "brand": "Mahle", "condition": "New", "price": 550, "currency": "EGP", "stock": 12, "images": ["placeholder"], "description": "Opens at 87 degrees celsius.", "sold_count": 8, "tags": ["cooling", "heat"]},
      {"oem": "GDB3332", "name": "TRW Brake Pad Set", "category": "Brakes", "type": "Pads", "brand": "TRW", "condition": "New", "price": 890, "currency": "EGP", "stock": 22, "images": ["placeholder"], "description": "COTEC coated brake pads.", "sold_count": 41, "tags": ["brakes", "standard"]}
    ]
  }
}

categories_data = {
  "Engine": ["SILZKGR8B8S", "W712/95", "941006"],
  "Brakes": ["0986494019", "09.A448.11", "GDB3332"],
  "Electrical": ["574012068", "439864", "64210"],
  "Suspension": ["339031", "2991601", "376045SP"],
  "Cooling": ["221-3600", "KP15680XS", "TX1887D"],
  "Fluids": ["152566", "15D5B8", "550046646"]
}

cars_data = {
  "Toyota": {
    "Corolla": {"2020": ["0986494019", "W712/95", "152566", "15D5B8", "64210"], "2021": ["0986494019", "W712/95", "152566", "15D5B8", "64210"], "2022": ["0986494019", "W712/95", "152566"]},
    "Camry": {"2019": ["SILZKGR8B8S", "574012068", "152566", "2991601"], "2020": ["SILZKGR8B8S", "574012068", "152566", "2991601"], "2021": ["SILZKGR8B8S", "574012068"]}
  },
  "Honda": {
    "Civic": {"2018": ["221-3600", "0986494019", "152566", "941006"], "2019": ["221-3600", "0986494019", "152566", "941006"], "2020": ["221-3600", "152566"]},
    "CR-V": {"2020": ["339031", "574012068", "15D5B8", "KP15680XS"], "2021": ["339031", "574012068", "15D5B8", "KP15680XS"], "2022": ["339031", "574012068"]}
  }
}

# --- CSS CONTENT (New) ---

CSS_CONTENT = """
:root {
    --primary-color: #ef4444; /* Red */
    --primary-hover: #dc2626;
    --dark-bg: #1a1a1a;
    --light-bg: #f8f9fa;
    --text-main: #1f2937;
    --text-muted: #6b7280;
    --border: #e5e7eb;
    --white: #ffffff;
}

body { font-family: 'Inter', sans-serif; background-color: var(--light-bg); margin: 0; color: var(--text-main); }
* { box-sizing: border-box; }
a { text-decoration: none; color: inherit; }
button { cursor: pointer; border: none; background: none; }

/* Layout Utilities */
.container { max-width: 1200px; margin: 0 auto; padding: 0 1.5rem; }
.flex { display: flex; }
.flex-col { flex-direction: column; }
.items-center { align-items: center; }
.justify-between { justify-content: space-between; }
.gap-6 { gap: 1.5rem; }
.gap-8 { gap: 2rem; }
.mt-auto { margin-top: auto; }
.w-full { width: 100%; }
.hidden { display: none; }

/* Header */
header { background: var(--white); border-bottom: 1px solid var(--border); position: sticky; top: 0; z-index: 50; height: 80px; display: flex; align-items: center; }
.header-wrapper { display: flex; justify-content: space-between; align-items: center; width: 100%; }
.logo { font-size: 1.5rem; font-weight: 700; letter-spacing: 0.1em; color: #111; }

.search-container { position: relative; flex: 1; max-width: 500px; margin: 0 2rem; }
.search-input { width: 100%; padding: 0.5rem 1rem 0.5rem 2.5rem; border: 1px solid #d1d5db; border-radius: 0.5rem; background-color: #f9fafb; outline: none; }
.search-input:focus { border-color: var(--primary-color); }
.search-icon { position: absolute; left: 0.75rem; top: 50%; transform: translateY(-50%); color: #9ca3af; }

.nav-icons { display: flex; gap: 1.5rem; align-items: center; }
.nav-icon { font-size: 1.25rem; color: #4b5563; transition: color 0.2s; position: relative; }
.nav-icon:hover { color: var(--primary-color); }
.badge { position: absolute; top: -8px; right: -8px; background: var(--primary-color); color: white; font-size: 0.7rem; font-weight: bold; height: 18px; width: 18px; border-radius: 50%; display: flex; justify-content: center; align-items: center; }

/* Main Layout */
.main-layout { display: flex; gap: 2rem; padding-top: 2rem; padding-bottom: 2rem; }

/* Sidebar */
aside { width: 250px; flex-shrink: 0; display: none; }
@media (min-width: 1024px) { aside { display: block; } }

.sidebar-box { background-color: var(--dark-bg); border-radius: 0.5rem; overflow: hidden; position: sticky; top: 100px; }
.sidebar-header { padding: 1rem 1.25rem; background-color: #111; border-bottom: 1px solid #374151; }
.sidebar-title { color: white; font-weight: bold; font-size: 0.875rem; text-transform: uppercase; margin: 0; }
.sidebar-nav { padding: 0.5rem 0; max-height: calc(100vh - 200px); overflow-y: auto; }
.sidebar-link { display: block; padding: 0.75rem 1.25rem; color: #d1d5db; border-left: 4px solid transparent; transition: all 0.2s; }
.sidebar-link:hover { background-color: #333; border-left-color: var(--primary-color); padding-left: 1.5rem; }
.sidebar-link.active { background-color: #333; border-left-color: var(--primary-color); padding-left: 1.5rem; font-weight: 600; color: white; }

/* Product Grid */
main { flex: 1; }
.page-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; }
.page-title { font-size: 1.25rem; font-weight: 700; margin: 0; }
.result-count { font-size: 0.875rem; color: var(--text-muted); }

.grid-container { display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 1.5rem; }

.product-card { background: white; border: 1px solid #f3f4f6; border-radius: 0.5rem; overflow: hidden; display: flex; flex-direction: column; cursor: pointer; transition: transform 0.2s, box-shadow 0.2s; }
.product-card:hover { transform: translateY(-4px); box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); }

.card-img-wrapper { position: relative; height: 180px; display: flex; justify-content: center; align-items: center; }
.card-badge { position: absolute; top: 0.5rem; right: 0.5rem; background: rgba(0,0,0,0.7); color: white; font-size: 0.7rem; font-weight: bold; padding: 0.25rem 0.5rem; border-radius: 0.25rem; text-transform: uppercase; }
.card-icon { font-size: 4rem; opacity: 0.7; }

.card-body { padding: 1rem; display: flex; flex-direction: column; flex: 1; }
.brand-text { font-size: 0.75rem; font-weight: 700; color: #9ca3af; text-transform: uppercase; }
.product-name { font-size: 0.95rem; font-weight: 600; margin: 0.25rem 0; line-height: 1.4; height: 2.8em; overflow: hidden; }
.card-footer { margin-top: auto; padding-top: 1rem; display: flex; justify-content: space-between; align-items: center; }
.price { font-size: 1.125rem; font-weight: 700; color: #111; }
.currency { font-size: 0.75rem; font-weight: 400; color: #6b7280; }
.btn-icon { background-color: var(--primary-color); color: white; padding: 0.5rem; border-radius: 9999px; transition: background 0.2s; }
.btn-icon:hover { background-color: var(--primary-hover); }

/* Detail Page */
.breadcrumb { margin-bottom: 2rem; font-size: 0.875rem; color: var(--text-muted); }
.breadcrumb a:hover { color: var(--primary-color); }
.detail-container { display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; background: white; padding: 2rem; border-radius: 0.75rem; border: 1px solid #f3f4f6; }
@media(max-width: 768px) { .detail-container { grid-template-columns: 1fr; } }

.detail-img-box { border-radius: 0.75rem; display: flex; justify-content: center; align-items: center; aspect-ratio: 1/1; position: relative; }
.detail-icon { font-size: 8rem; opacity: 0.8; }
.thumbnails { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: 1rem; }
.thumb { aspect-ratio: 1/1; background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 0.5rem; display: flex; justify-content: center; align-items: center; color: #d1d5db; }

.detail-info { display: flex; flex-direction: column; }
.detail-title { font-size: 1.875rem; font-weight: 700; margin: 0 0 0.5rem 0; }
.rating { color: #fbbf24; font-size: 0.875rem; margin-bottom: 1.5rem; }
.detail-price { font-size: 2rem; font-weight: 700; margin-bottom: 1.5rem; }
.description { color: #4b5563; line-height: 1.6; margin-bottom: 2rem; }

.actions { margin-top: auto; }
.qty-row { display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem; }
.qty-selector { display: flex; border: 1px solid #d1d5db; border-radius: 0.5rem; overflow: hidden; }
.qty-btn { padding: 0.5rem 1rem; background: #f9fafb; transition: background 0.2s; }
.qty-btn:hover { background: #e5e7eb; }
.qty-val { padding: 0.5rem 1rem; font-weight: bold; min-width: 40px; text-align: center; }
.stock-status { color: #16a34a; font-weight: 500; font-size: 0.875rem; }

.cart-row { display: flex; gap: 1rem; margin-bottom: 1rem; }
.btn-add { flex: 1; background: #111; color: white; padding: 1rem; border-radius: 0.5rem; font-weight: bold; display: flex; align-items: center; justify-content: center; gap: 0.5rem; transition: background 0.2s; }
.btn-add:hover { background: #333; }
.btn-buy { width: 100%; border: 2px solid #e5e7eb; padding: 0.75rem; border-radius: 0.5rem; font-weight: bold; color: #374151; transition: all 0.2s; }
.btn-buy:hover { border-color: #111; color: #111; }

.features-box { margin-top: 3rem; background: white; border-radius: 0.75rem; border: 1px solid #f3f4f6; overflow: hidden; }
.tabs { display: flex; border-bottom: 1px solid #e5e7eb; background: #f9fafb; }
.tab { padding: 1rem 2rem; font-weight: 500; color: #6b7280; }
.tab.active { background: white; border-top: 2px solid var(--primary-color); color: #111; font-weight: 700; }
.tab-content { padding: 2rem; color: #4b5563; }

/* Colors Helpers (for categories) */
.bg-gray-200 { background-color: #e5e7eb; color: #4b5563; }
.bg-red-50 { background-color: #fef2f2; color: #ef4444; }
.bg-yellow-50 { background-color: #fefce8; color: #d97706; }
.bg-blue-50 { background-color: #eff6ff; color: #3b82f6; }
.bg-cyan-50 { background-color: #ecfeff; color: #06b6d4; }
.bg-amber-50 { background-color: #fffbeb; color: #d97706; }
"""

# --- FILE CONTENT STRINGS ---

MODEL_PY_CONTENT = """
import json
from pathlib import Path

class DataRepository:
    def __init__(self):
        base_dir = Path(__file__).parent
        self.data_folder = base_dir / 'data'

    def load_json(self, filename):
        file_path = self.data_folder / filename
        with file_path.open('r', encoding='utf-8') as f:
            return json.load(f)

    def get_all_products(self):
        # Flatten sellers -> products and add IDs
        sellers = self.load_json('sellers_inventory.json')
        all_products = []
        for seller_id, seller_data in sellers.items():
            for product in seller_data['products']:
                product['seller_name'] = seller_data['name']
                # Generate unique ID: SellerID_OEM (e.g., SELLER_01_152566)
                product['id'] = f"{seller_id}_{product['oem']}"
                all_products.append(product)
        return all_products

    def get_product_by_id(self, product_id):
        # Fetch all and filter (Simple implementation for JSON)
        products = self.get_all_products()
        for p in products:
            if p['id'] == product_id:
                return p
        return None

    def get_categories(self):
        return self.load_json('categories.json')
"""

CONTROLLER_PY_CONTENT = """
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
"""

APP_PY_CONTENT = """
from flask import Flask
from controllers import shop_controller

app = Flask(__name__)
app.register_blueprint(shop_controller)

if __name__ == '__main__':
    app.run(debug=True)
"""

HTML_INDEX_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ELHERAFEEN - Auto Parts</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>

    <header>
        <div class="container header-wrapper">
            <a href="/" class="logo">ELHERAFEEN</a>
            <div class="search-container">
                <i class="fas fa-search search-icon"></i>
                <input type="text" id="searchInput" placeholder="Search..." class="search-input">
            </div>
            <div class="nav-icons">
                <button class="nav-icon"><i class="far fa-user"></i></button>
                <button class="nav-icon">
                    <i class="fas fa-shopping-cart"></i>
                    <span id="cartCount" class="badge" style="display:none">0</span>
                </button>
            </div>
        </div>
    </header>

    <div class="container main-layout">
        <aside>
            <div class="sidebar-box">
                <div class="sidebar-header"><h3 class="sidebar-title">Categories</h3></div>
                <nav class="sidebar-nav">
                    <a href="#" class="sidebar-link active">All Products</a>
                    {% for cat in categories %}
                    <a href="#" class="sidebar-link">{{ cat }}</a>
                    {% endfor %}
                </nav>
            </div>
        </aside>

        <main>
            <div class="page-header">
                <h2 class="page-title" id="categoryTitle">All Products</h2>
                <span class="result-count" id="resultCount">Showing {{ products|length }} results</span>
            </div>
            <div id="productGrid" class="grid-container"></div>
        </main>
    </div>

    <!-- JavaScript removed: render products and filtering now performed server-side by Flask -->
</body>
</html>
"""

HTML_DETAIL_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ product.name }} - ELHERAFEEN</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <header>
        <div class="container header-wrapper">
            <a href="/" class="logo">ELHERAFEEN</a>
            <div class="nav-icons">
                <a href="/" class="nav-icon" style="font-size:1rem; text-decoration:none">Home</a>
                <button class="nav-icon"><i class="fas fa-shopping-cart"></i></button>
            </div>
        </div>
    </header>

    <div class="container" style="padding-top:2rem; padding-bottom:4rem;">
        <nav class="breadcrumb">
            <a href="/">Home</a> <span>/</span>
            <span>{{ product.category }}</span> <span>/</span>
            <span style="color:var(--text-main); font-weight:500">{{ product.name }}</span>
        </nav>

        <div class="detail-container">
            <!-- Left: Images -->
            <div>
                {% set icons = {'Engine': 'fa-cogs', 'Brakes': 'fa-compact-disc', 'Electrical': 'fa-bolt', 'Suspension': 'fa-spring', 'Cooling': 'fa-fan', 'Fluids': 'fa-oil-can'} %}
                {% set colors = {'Engine': 'bg-gray-200', 'Brakes': 'bg-red-50', 'Electrical': 'bg-yellow-50', 'Suspension': 'bg-blue-50', 'Cooling': 'bg-cyan-50', 'Fluids': 'bg-amber-50'} %}
                
                <div class="detail-img-box {{ colors[product.category] }}">
                    <i class="fas {{ icons[product.category] or 'fa-box' }} detail-icon"></i>
                    <span class="card-badge" style="top:1rem; left:1rem; right:auto;">{{ product.condition }}</span>
                </div>
                <div class="thumbnails">
                    <div class="thumb"><i class="fas fa-camera"></i></div>
                    <div class="thumb"><i class="fas fa-box-open"></i></div>
                    <div class="thumb"><i class="fas fa-tag"></i></div>
                </div>
            </div>

            <!-- Right: Info -->
            <div class="detail-info">
                <div class="brand-text" style="color:var(--primary-color); font-size:0.875rem;">{{ product.brand }}</div>
                <h1 class="detail-title">{{ product.name }}</h1>
                <div class="rating">
                    <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star-half-alt"></i>
                    <span style="color:#6b7280; margin-left:0.5rem">({{ product.sold_count }} sold)</span>
                    <span style="color:#d1d5db; margin:0 0.5rem">|</span>
                    <span style="color:#6b7280">OEM: <b>{{ product.oem }}</b></span>
                </div>

                <div class="detail-price">{{ product.price }} <span class="currency" style="font-size:1.25rem">{{ product.currency }}</span></div>

                <div class="description">
                    <p>{{ product.description }}</p>
                </div>

                <div class="actions">
                    <div class="qty-row">
                        <div class="qty-selector">
                            <button class="qty-btn">-</button>
                            <span id="qty" class="qty-val">1</span>
                            <button class="qty-btn">+</button>
                        </div>
                        <div class="stock-status"><i class="fas fa-check-circle"></i> In Stock ({{ product.stock }})</div>
                    </div>

                    <div class="cart-row">
                        <button class="btn-add"><i class="fas fa-shopping-cart"></i> Add to Cart</button>
                        <button style="width:50px; border:1px solid #d1d5db; border-radius:0.5rem; color:#4b5563"><i class="far fa-heart"></i></button>
                    </div>
                    <button class="btn-buy">Buy Now</button>
                </div>
                
                <div style="margin-top:2rem; padding-top:1.5rem; border-top:1px solid #f3f4f6; color:#6b7280; font-size:0.875rem; display:flex; flex-direction:column; gap:0.75rem;">
                    <div><i class="fas fa-truck" style="width:20px"></i> Free shipping on orders over 1000 EGP</div>
                    <div><i class="fas fa-undo" style="width:20px"></i> 30-Day Returns Policy</div>
                    <div><i class="fas fa-shield-alt" style="width:20px"></i> 1 Year Warranty included</div>
                </div>
            </div>
        </div>

        <div class="features-box">
            <div class="tabs">
                <div class="tab active">Description</div>
                <div class="tab">Specifications</div>
                <div class="tab">Reviews (3)</div>
            </div>
            <div class="tab-content">
                <h3 style="margin-top:0;">Product Description</h3>
                <p>{{ product.description }}</p>
                <p>The {{ product.brand }} {{ product.name }} is engineered to meet or exceed OEM specifications. Designed for durability and performance.</p>
                
                <h3>Key Features</h3>
                <ul style="padding-left:1.5rem">
                    <li>Brand: {{ product.brand }}</li>
                    <li>Type: {{ product.type }}</li>
                    <li>Category: {{ product.category }}</li>
                    <li>Condition: {{ product.condition }}</li>
                    <li>Seller: {{ product.seller_name }}</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- JavaScript removed: use server-side form/select for quantity -->
</body>
</html>
"""

README_CONTENT = """
# CSAI 203 Course Project - Team ELHERAFEEN

## Description
This is an Auto Parts E-commerce system built with Flask and HTML/CSS (No frameworks).
It implements the MVC architecture.

## How to Run
1. Install Flask: `pip install flask`
2. Navigate to src: `cd src`
3. Run the app: `python app.py`
4. Open browser: `http://127.0.0.1:5000`
"""

# --- DIRECTORY CREATION ---
def create_structure():
    dirs = [
        PROJECT_ROOT / "src" / "data",
        PROJECT_ROOT / "src" / "templates",
        PROJECT_ROOT / "src" / "static",
        PROJECT_ROOT / "docs",
        PROJECT_ROOT / "tests",
        PROJECT_ROOT / "deployment",
    ]
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
    print(f"Created directory structure in {PROJECT_ROOT}/")

def write_file(path, content):
    full_path = PROJECT_ROOT / path
    full_path.write_text(content.strip(), encoding='utf-8')
    print(f"Created {path}")

def generate_files():
    # 1. JSON Data
    write_file("src/data/sellers_inventory.json", json.dumps(sellers_inventory, indent=2))
    write_file("src/data/categories.json", json.dumps(categories_data, indent=2))
    write_file("src/data/cars.json", json.dumps(cars_data, indent=2))

    # 2. Python MVC Files
    write_file("src/models.py", MODEL_PY_CONTENT)
    write_file("src/controllers.py", CONTROLLER_PY_CONTENT)
    write_file("src/app.py", APP_PY_CONTENT)

    # 3. HTML Views (Now without Tailwind)
    write_file("src/templates/index.html", HTML_INDEX_CONTENT)
    write_file("src/templates/product_detail.html", HTML_DETAIL_CONTENT)

    # 4. Static Assets (New)
    write_file("src/static/style.css", CSS_CONTENT)

    # 5. Meta
    write_file("README.md", README_CONTENT)
    write_file("deployment/requirements.txt", "flask\npytest")
    write_file("tests/test_basic.py", "def test_dummy(): assert True")
    write_file("docs/SRS.txt", "SRS Placeholder")

if __name__ == "__main__":
    create_structure()
    generate_files()
    print("\\n✅ Project regenerated with Pure CSS and Product Details Page!")
    print(f"Go to '{PROJECT_ROOT}/src' and run 'python app.py'")