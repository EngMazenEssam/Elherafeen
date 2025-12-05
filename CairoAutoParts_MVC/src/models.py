import json
from pathlib import Path

class DataRepository:
    def __init__(self):
        base_dir = Path(__file__).parent
        self.data_folder = base_dir / 'data'
        self._products_cache = None

    def load_json(self, filename):
        file_path = self.data_folder / filename
        with file_path.open('r', encoding='utf-8') as f:
            return json.load(f)

    def get_all_products(self):
        # Flatten sellers -> products and add IDs
        if self._products_cache is None:
            sellers = self.load_json('sellers_inventory.json')
            all_products = []
            for seller_id, seller_data in sellers.items():
                for product in seller_data['products']:
                    product['seller_name'] = seller_data['name']
                    # Generate unique ID: SellerID_OEM (e.g., SELLER_01_152566)
                    product['id'] = f"{seller_id}_{product['oem']}"
                    all_products.append(product)
            self._products_cache = all_products
        return self._products_cache

    def get_product_by_id(self, product_id):
        # Fetch all and filter (Simple implementation for JSON)
        products = self.get_all_products()
        for p in products:
            if p['id'] == product_id:
                return p
        return None

    def get_categories(self):
        categories_data = self.load_json('categories.json')
        return list(categories_data.keys())

    def get_products_by_category(self, category):
        products = self.get_all_products()
        if category == 'All':
            return products
        return [p for p in products if p.get('category') == category]

    def search_products(self, search_term):
        products = self.get_all_products()
        term = search_term.lower()
        return [p for p in products if term in p.get('name', '').lower() or term in p.get('oem', '').lower()]

    def get_products_filtered(self, category=None, search=None):
        products = self.get_all_products()
        
        if search:
            term = search.lower()
            products = [p for p in products if term in p.get('name', '').lower() or term in p.get('oem', '').lower()]
        
        if category and category != 'All':
            products = [p for p in products if p.get('category') == category]
        
        return products