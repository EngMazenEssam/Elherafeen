from app.repository.product_repository import iter_all_products


def build_product(seller_id, seller, product):
    p = product.copy()
    p["seller_id"] = seller_id
    p["seller_name"] = seller.get("name")
    p["id"] = f"{seller_id}_{p.get('oem')}"
    return p


def get_all_products():
    return [
        build_product(seller_id, seller, product)
        for seller_id, seller, product in iter_all_products()
    ]


def get_product_by_id(product_id):
    for seller_id, seller, product in iter_all_products():
        if f"{seller_id}_{product.get('oem')}" == product_id:
            return build_product(seller_id, seller, product)
    return None


def filter_products(category=None, search=None):
    products = get_all_products()

    if search:
        search = search.lower()
        products = [
            p for p in products
            if search in p["name"].lower()
            or search in p["oem"].lower()
        ]

    if category and category != "All":
        products = [p for p in products if p["category"] == category]

    return products
