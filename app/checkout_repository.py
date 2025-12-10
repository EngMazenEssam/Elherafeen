import json
from pathlib import Path


def get_data_folder():
    current_file = Path(__file__)

    parent_folder = current_file.parent

    base_folder = parent_folder.parent

    data_folder = base_folder / "data"

    return data_folder


def load_cart():
    data_folder = get_data_folder()
    cart_file = data_folder / "cart.json"

    try:
        with open(cart_file, "r", encoding="utf-8") as f:
            cart_data = json.load(f)

        if "items" not in cart_data:
            cart_data["items"] = []

        if "total_items" not in cart_data:
            cart_data["total_items"] = 0

        if "total_price" not in cart_data:
            cart_data["total_price"] = 0

        return cart_data

    except FileNotFoundError:
        empty_cart = {
            "items": [],
            "total_items": 0,
            "total_price": 0,
        }
        return empty_cart


def load_products():
    data_folder = get_data_folder()
    products_file = data_folder / "sellers_inventory.json"

    try:
        with open(products_file, "r", encoding="utf-8") as f:
            sellers_data = json.load(f)

        all_products = []


        for seller_id, seller_info in sellers_data.items():
            seller_name = seller_info.get("name", "")

            products_list = seller_info.get("products", [])
            for product in products_list:
                product["seller_name"] = seller_name

                oem_value = product.get("oem")
                product["id"] = f"{seller_id}_{oem_value}"

                all_products.append(product)

        return all_products

    except FileNotFoundError:
        return []


def save_orders(orders):
    data_folder = get_data_folder()
    orders_file = data_folder / "orders.json"

    with open(orders_file, "w", encoding="utf-8") as f:
        json.dump(orders, f, indent=2)


def clear_cart():
    data_folder = get_data_folder()
    cart_file = data_folder / "cart.json"

    empty_cart = {
        "items": [],
        "total_items": 0,
        "total_price": 0,
    }

    with open(cart_file, "w", encoding="utf-8") as f:
        json.dump(empty_cart, f, indent=2)
