import os
import json

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA_DIR = os.path.join(BASE_DIR, "data")
PRODUCTS_FILE = os.path.join(DATA_DIR, "products.json")

def _load_json(path, default):
    if not os.path.exists(path):
        return default
    with open(path, encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return default

def load_products_raw():
    return _load_json(PRODUCTS_FILE, default={})

def iter_all_products():
    data = load_products_raw()
    for seller_id, seller in data.items():
        for p in seller.get("products", []):
            yield seller_id, seller, p
