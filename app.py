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
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; background-color: #f8f9fa; }
        .custom-scroll::-webkit-scrollbar { width: 6px; }
        .custom-scroll::-webkit-scrollbar-track { background: #1a1a1a; }
        .custom-scroll::-webkit-scrollbar-thumb { background: #333; border-radius: 3px; }
        .product-card { transition: transform 0.2s ease, box-shadow 0.2s ease; cursor: pointer; }
        .product-card:hover { transform: translateY(-4px); box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1); }
        .sidebar-link.active { background-color: #333; border-left: 4px solid #ef4444; padding-left: 16px; font-weight: 600; }
        .sidebar-link { transition: all 0.2s; border-left: 4px solid transparent; }
        .sidebar-link:hover { background-color: #333; border-left: 4px solid #ef4444; padding-left: 16px; }
    </style>
</head>
<body class="text-gray-800">

    <header class="bg-white border-b border-gray-200 sticky top-0 z-50">
        <div class="container mx-auto px-6 h-20 flex items-center justify-between">
            <h1 class="text-2xl font-bold tracking-widest text-gray-900">ELHERAFEEN</h1>
            <div class="hidden md:flex flex-1 mx-12 relative max-w-xl">
                <span class="absolute inset-y-0 left-0 pl-3 flex items-center"><i class="fas fa-search text-gray-400"></i></span>
                <input type="text" id="searchInput" placeholder="Search..." class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-red-500 bg-gray-50">
            </div>
            <div class="flex items-center space-x-6">
                <button class="text-gray-600 hover:text-red-500"><i class="far fa-user text-xl"></i></button>
                <button class="text-gray-600 hover:text-red-500 relative">
                    <i class="fas fa-shopping-cart text-xl"></i>
                    <span id="cartCount" class="absolute -top-2 -right-2 bg-red-500 text-white text-xs font-bold rounded-full h-5 w-5 flex items-center justify-center opacity-0 transition-opacity">0</span>
                </button>
            </div>
        </div>
    </header>

    <div class="container mx-auto px-6 py-8 flex flex-col lg:flex-row gap-8">
        <aside class="hidden lg:block w-64 flex-shrink-0">
            <div class="bg-[#1a1a1a] text-gray-300 rounded-lg overflow-hidden shadow-lg sticky top-24">
                <div class="px-5 py-4 border-b border-gray-700 bg-[#111]"><h3 class="text-white font-bold text-sm uppercase">Categories</h3></div>
                <nav class="flex flex-col py-2 custom-scroll max-h-[calc(100vh-200px)] overflow-y-auto">
                    <a href="#" class="sidebar-link active block px-5 py-3 text-sm font-medium text-gray-300 hover:text-white" onclick="filterCategory(event, 'All')">All Products</a>
                    {% for cat in categories %}
                    <a href="#" class="sidebar-link block px-5 py-3 text-sm font-medium text-gray-300 hover:text-white capitalize" onclick="filterCategory(event, '{{ cat }}')">{{ cat }}</a>
                    {% endfor %}
                </nav>
            </div>
        </aside>

        <main class="flex-1">
            <div class="flex justify-between items-center mb-6">
                <h2 class="text-xl font-bold text-gray-800" id="categoryTitle">All Products</h2>
                <span class="text-sm text-gray-500" id="resultCount">Showing {{ products|length }} results</span>
            </div>
            <div id="productGrid" class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-6"></div>
        </main>
    </div>

    <script>
        const allProducts = {{ products | tojson }};
        const productGrid = document.getElementById('productGrid');
        const categoryTitle = document.getElementById('categoryTitle');
        const resultCount = document.getElementById('resultCount');

        function getImage(category) {
            const icons = {'Engine': 'fa-cogs', 'Brakes': 'fa-compact-disc', 'Electrical': 'fa-bolt', 'Suspension': 'fa-spring', 'Cooling': 'fa-fan', 'Fluids': 'fa-oil-can'};
            const colors = {'Engine': 'bg-gray-200 text-gray-600', 'Brakes': 'bg-red-100 text-red-500', 'Electrical': 'bg-yellow-100 text-yellow-600', 'Suspension': 'bg-blue-100 text-blue-500', 'Cooling': 'bg-cyan-100 text-cyan-500', 'Fluids': 'bg-amber-100 text-amber-600'};
            return `<div class="h-48 w-full ${colors[category]||'bg-gray-100'} flex items-center justify-center"><i class="fas ${icons[category]||'fa-box'} text-6xl opacity-80"></i></div>`;
        }

        function renderProducts(products) {
            productGrid.innerHTML = '';
            resultCount.textContent = `Showing ${products.length} results`;
            products.forEach(p => {
                const card = document.createElement('div');
                card.className = 'product-card bg-white rounded-lg overflow-hidden border border-gray-100 flex flex-col h-full relative group';
                // Link to product detail page
                card.onclick = () => window.location.href = `/product/${p.id}`;
                card.innerHTML = `
                    <div class="relative overflow-hidden">${getImage(p.category)}
                        <span class="absolute top-2 right-2 bg-black bg-opacity-70 text-white text-[10px] font-bold px-2 py-1 rounded uppercase">${p.condition}</span>
                    </div>
                    <div class="p-4 flex flex-col flex-1">
                        <div class="mb-2">
                            <span class="text-xs font-bold text-gray-400 uppercase">${p.brand}</span>
                            <h3 class="text-gray-800 font-semibold text-sm mt-1 h-10 overflow-hidden line-clamp-2">${p.name}</h3>
                        </div>
                        <div class="mt-auto pt-4 flex justify-between items-center">
                            <div><span class="block text-xs text-gray-400">Price</span><span class="text-lg font-bold text-gray-900">${p.price} <span class="text-xs font-normal">${p.currency}</span></span></div>
                            <button class="bg-red-500 text-white p-2 rounded-full hover:bg-red-600 transition shadow-sm"><i class="fas fa-shopping-cart text-sm"></i></button>
                        </div>
                    </div>`;
                productGrid.appendChild(card);
            });
        }

        function filterCategory(e, cat) {
            e.preventDefault();
            document.querySelectorAll('.sidebar-link').forEach(el => el.classList.remove('active'));
            e.target.classList.add('active');
            categoryTitle.textContent = cat === 'All' ? 'All Products' : cat;
            renderProducts(cat === 'All' ? allProducts : allProducts.filter(p => p.category === cat));
        }

        renderProducts(allProducts);
        // Basic search
        document.getElementById('searchInput').addEventListener('input', (e) => {
            const term = e.target.value.toLowerCase();
            renderProducts(allProducts.filter(p => p.name.toLowerCase().includes(term) || p.oem.toLowerCase().includes(term)));
        });
    </script>
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
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>body { font-family: 'Inter', sans-serif; background-color: #f8f9fa; }</style>
</head>
<body class="text-gray-800">
    <!-- Header -->
    <header class="bg-white border-b border-gray-200 sticky top-0 z-50">
        <div class="container mx-auto px-6 h-20 flex items-center justify-between">
            <a href="/" class="text-2xl font-bold tracking-widest text-gray-900">ELHERAFEEN</a>
            <div class="flex items-center space-x-6">
                <a href="/" class="text-gray-600 hover:text-red-500 font-medium">Home</a>
                <button class="text-gray-600 hover:text-red-500 relative"><i class="fas fa-shopping-cart text-xl"></i></button>
            </div>
        </div>
    </header>

    <div class="container mx-auto px-6 py-10">
        <!-- Breadcrumb -->
        <nav class="text-sm text-gray-500 mb-8">
            <a href="/" class="hover:text-red-500">Home</a> <span class="mx-2">/</span>
            <span class="hover:text-red-500">{{ product.category }}</span> <span class="mx-2">/</span>
            <span class="text-gray-900 font-medium">{{ product.name }}</span>
        </nav>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-12 bg-white p-8 rounded-xl shadow-sm border border-gray-100">
            <!-- Left: Image Section -->
            <div class="space-y-4">
                {% set icons = {'Engine': 'fa-cogs', 'Brakes': 'fa-compact-disc', 'Electrical': 'fa-bolt', 'Suspension': 'fa-spring', 'Cooling': 'fa-fan', 'Fluids': 'fa-oil-can'} %}
                {% set colors = {'Engine': 'bg-gray-200 text-gray-600', 'Brakes': 'bg-red-50 text-red-500', 'Electrical': 'bg-yellow-50 text-yellow-600', 'Suspension': 'bg-blue-50 text-blue-500', 'Cooling': 'bg-cyan-50 text-cyan-500', 'Fluids': 'bg-amber-50 text-amber-600'} %}
                
                <div class="aspect-square w-full rounded-xl {{ colors[product.category] }} flex items-center justify-center relative overflow-hidden group">
                    <i class="fas {{ icons[product.category] or 'fa-box' }} text-9xl opacity-80 transition transform group-hover:scale-110 duration-500"></i>
                    <div class="absolute top-4 left-4">
                         <span class="bg-black text-white text-xs font-bold px-3 py-1 rounded uppercase tracking-wider">{{ product.condition }}</span>
                    </div>
                </div>
                <!-- Thumbnails (Simulated) -->
                <div class="grid grid-cols-3 gap-4">
                    <div class="aspect-square rounded-lg bg-gray-50 border border-gray-200 cursor-pointer hover:border-red-500 transition flex items-center justify-center"><i class="fas fa-camera text-gray-300"></i></div>
                    <div class="aspect-square rounded-lg bg-gray-50 border border-gray-200 cursor-pointer hover:border-red-500 transition flex items-center justify-center"><i class="fas fa-box-open text-gray-300"></i></div>
                    <div class="aspect-square rounded-lg bg-gray-50 border border-gray-200 cursor-pointer hover:border-red-500 transition flex items-center justify-center"><i class="fas fa-tag text-gray-300"></i></div>
                </div>
            </div>

            <!-- Right: Details Section -->
            <div class="flex flex-col">
                <div class="mb-1 text-sm font-bold text-red-500 uppercase tracking-wider">{{ product.brand }}</div>
                <h1 class="text-3xl font-bold text-gray-900 mb-2">{{ product.name }}</h1>
                <div class="flex items-center space-x-2 mb-6 text-sm">
                    <div class="flex text-yellow-400 text-xs">
                        <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star-half-alt"></i>
                    </div>
                    <span class="text-gray-500">({{ product.sold_count }} sold)</span>
                    <span class="text-gray-300">|</span>
                    <span class="text-gray-500">OEM: <span class="font-mono text-gray-700">{{ product.oem }}</span></span>
                </div>

                <div class="text-3xl font-bold text-gray-900 mb-6">{{ product.price }} <span class="text-lg font-normal text-gray-500">{{ product.currency }}</span></div>

                <div class="prose prose-sm text-gray-600 mb-8">
                    <p>{{ product.description }}</p>
                </div>

                <!-- Add to Cart / Actions -->
                <div class="space-y-4 mt-auto">
                    <div class="flex items-center space-x-4">
                         <div class="flex items-center border border-gray-300 rounded-lg">
                            <button class="px-4 py-2 hover:bg-gray-100 transition" onclick="updateQty(-1)">-</button>
                            <span id="qty" class="px-4 font-bold">1</span>
                            <button class="px-4 py-2 hover:bg-gray-100 transition" onclick="updateQty(1)">+</button>
                        </div>
                        <div class="text-sm text-green-600 font-medium"><i class="fas fa-check-circle mr-1"></i> In Stock ({{ product.stock }})</div>
                    </div>

                    <div class="flex gap-4">
                        <button class="flex-1 bg-black text-white py-4 rounded-lg font-bold hover:bg-gray-800 transition flex items-center justify-center gap-2">
                            <i class="fas fa-shopping-cart"></i> Add to Cart
                        </button>
                        <button class="w-14 h-14 border border-gray-300 rounded-lg flex items-center justify-center hover:bg-gray-50 hover:text-red-500 transition">
                            <i class="far fa-heart text-xl"></i>
                        </button>
                    </div>
                    <button class="w-full border-2 border-gray-200 text-gray-700 font-bold py-3 rounded-lg hover:border-gray-900 hover:text-black transition">Buy Now</button>
                </div>
                
                <div class="mt-8 pt-8 border-t border-gray-100 space-y-3 text-sm text-gray-500">
                    <div class="flex items-center gap-3"><i class="fas fa-truck text-gray-400 w-5"></i> Free shipping on orders over 1000 EGP</div>
                    <div class="flex items-center gap-3"><i class="fas fa-undo text-gray-400 w-5"></i> 30-Day Returns Policy</div>
                    <div class="flex items-center gap-3"><i class="fas fa-shield-alt text-gray-400 w-5"></i> 1 Year Warranty included</div>
                </div>
            </div>
        </div>

        <!-- Description / Specs Tabs -->
        <div class="mt-12 bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
            <div class="flex border-b border-gray-200 bg-gray-50">
                <button class="px-8 py-4 font-bold text-gray-900 bg-white border-t-2 border-red-500">Description</button>
                <button class="px-8 py-4 font-medium text-gray-500 hover:text-gray-800">Specifications</button>
                <button class="px-8 py-4 font-medium text-gray-500 hover:text-gray-800">Reviews (3)</button>
            </div>
            <div class="p-8">
                <h3 class="text-lg font-bold mb-4">Product Description</h3>
                <p class="text-gray-600 mb-4">{{ product.description }}</p>
                <p class="text-gray-600">The {{ product.brand }} {{ product.name }} is engineered to meet or exceed OEM specifications. Designed for durability and performance, it is the perfect choice for your vehicle maintenance needs.</p>
                
                <h3 class="text-lg font-bold mt-8 mb-4">Key Features</h3>
                <ul class="list-disc list-inside space-y-2 text-gray-600">
                    <li>Brand: {{ product.brand }}</li>
                    <li>Type: {{ product.type }}</li>
                    <li>Category: {{ product.category }}</li>
                    <li>Condition: {{ product.condition }}</li>
                    <li>Seller: {{ product.seller_name }}</li>
                </ul>
            </div>
        </div>
    </div>

    <script>
        function updateQty(change) {
            const el = document.getElementById('qty');
            let val = parseInt(el.textContent);
            val = Math.max(1, Math.min(val + change, {{ product.stock }}));
            el.textContent = val;
        }
    </script>
</body>
</html>
"""

README_CONTENT = """
# CSAI 203 Course Project - Team ELHERAFEEN

## Description
This is an Auto Parts E-commerce system built with Flask and HTML/TailwindCSS.
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

    # 3. HTML Views
    write_file("src/templates/index.html", HTML_INDEX_CONTENT)
    write_file("src/templates/product_detail.html", HTML_DETAIL_CONTENT)

    # 4. Meta
    write_file("README.md", README_CONTENT)
    write_file("deployment/requirements.txt", "flask\npytest")
    write_file("tests/test_basic.py", "def test_dummy(): assert True")
    write_file("docs/SRS.txt", "SRS Placeholder")

if __name__ == "__main__":
    create_structure()
    generate_files()
    print("\\n✅ Project regenerated with Product Details Page!")
    print(f"Go to '{PROJECT_ROOT}/src' and run 'python app.py'")