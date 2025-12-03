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