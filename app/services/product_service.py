import os
import json
from app.repository.product_repository import iter_all_products

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA_DIR = os.path.join(BASE_DIR, "data")
CATEGORIES_FILE = os.path.join(DATA_DIR, "categories.json")

def build_product_object(seller_id, seller, product):
    p = product.copy()
    p["seller_name"] = seller.get("name")
    p["id"] = f"{seller_id}_{p.get('oem')}"
    return p

def get_all_products():
    products = []
    for seller_id, seller, product in iter_all_products():
        products.append(build_product_object(seller_id, seller, product))
    return products

def get_product_by_id(product_id: str):
    for seller_id, seller, product in iter_all_products():
        pid = f"{seller_id}_{product.get('oem')}"
        if pid == product_id:
            return build_product_object(seller_id, seller, product)
    return None

def get_categories():
    if not os.path.exists(CATEGORIES_FILE):
        return []
    with open(CATEGORIES_FILE, encoding="utf-8") as f:
        data = json.load(f)
    return list(data.keys())

def filter_products(category=None, search=None):
    products = get_all_products()
    if search:
        term = search.lower()
        products = [
            p for p in products
            if term in p.get("name", "").lower()
            or term in p.get("oem", "").lower()
        ]
    if category and category != "All":
        products = [p for p in products if p.get("category") == category]
    return products
