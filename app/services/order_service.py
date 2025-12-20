import json
import os
from app.services.product_service import get_product

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "data")


def load_orders():
    with open(os.path.join(DATA_DIR, "orders.json"), "r", encoding="utf-8") as f:
        return json.load(f)


def get_orders_for_user(email):
    orders = load_orders()
    user_orders = []

    for order in orders:
        if order["user_email"] != email:
            continue

        resolved_items = []
        total_price = 0

        for item in order["items"]:
            product = get_product(item["seller_id"], item["oem"])
            if not product:
                continue

            item_total = product["price"] * item["quantity"]
            total_price += item_total

            resolved_items.append({
                "name": product["name"],
                "brand": product["brand"],
                "price": product["price"],
                "quantity": item["quantity"],
                "total": item_total
            })

        user_orders.append({
            "order_id": order["order_id"],
            "date": order["date"],
            "status": order["status"],
            "items": resolved_items,
            "total": total_price
        })

    return user_orders
