import json
from pathlib import Path

class DataRepository:
    def __init__(self):
        base_dir = Path(__file__).parent
        self.data_folder = base_dir / 'data'
        self._products_board = None

    def load_json(self, filename):
        file_path = self.data_folder / filename
        with open(file_path, 'r') as f:
            return json.load(f)

    def get_all_products(self):
        if self._products_board is None:
            sellers = self.load_json('sellers_inventory.json')
            all_products = []
            for seller_id, seller_data in sellers.items():
                for product in seller_data['products']:
                    product['seller_name'] = seller_data['name']
                    product['id'] = f"{seller_id}_{product['oem']}"
                    all_products.append(product)
            self._products_board = all_products  
        return self._products_board

    def get_product_by_id(self, product_id):
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
        
        filtered_products = []
        for p in products:
            if p.get('category') == category:
                filtered_products.append(p)
        return filtered_products

    def search_products(self, search_term):
        products = self.get_all_products()
        term = search_term.lower()
        results = []
        for p in products:
            name = p.get('name', '').lower()
            oem = p.get('oem', '').lower()
            if term in name or term in oem:
                results.append(p)
        return results

    def get_products_filtered(self, category=None, search=None):
        products = self.get_all_products()
        
        if search:
            term = search.lower()
            filtered = []
            for p in products:
                name = p.get('name', '').lower()
                oem = p.get('oem', '').lower()
                if term in name or term in oem:
                    filtered.append(p)
            products = filtered
        
        if category and category != 'All':
            filtered = []
            for p in products:
                if p.get('category') == category:
                    filtered.append(p)
            products = filtered
        
        return products

    def load_cart(self):
        try:
            return self.load_json('cart.json')
        except FileNotFoundError:
            return {"items": []}

    def save_cart(self, cart_data):
        file_path = self.data_folder / 'cart.json'
        with open(file_path, 'w') as f:
            json.dump(cart_data, f, indent=2)
    
    def get_cart_items(self):
        cart = self.load_cart()
        all_products = self.get_all_products()
        result = []
        
        for i in cart['items']:
            oem = i['oem']
            qty = i['quantity']
            matching_product = None
            
            for product in all_products:
                if product['oem'] == oem:
                    matching_product = product
                    break
            
            if matching_product:
                item = matching_product.copy()
                item['quantity'] = qty
                item['product_id'] = item['id']
                result.append(item)
        
        return result
