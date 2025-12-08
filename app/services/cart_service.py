from app.repository.cart_repository import load_cart_raw, save_cart_raw
from app.repository.product_repository import load_products_raw


def build_products_by_oem():
    data = load_products_raw()
    products_by_oem = {}

    for seller_id, seller in data.items():
        seller_name = seller.get("name")
        for p in seller.get("products", []):
            oem = p.get("oem")
            if not oem:
                continue

            product_data = p.copy()
            product_data["seller_id"] = seller_id
            product_data["seller_name"] = seller_name
            products_by_oem[oem] = product_data

    return products_by_oem


def get_cart_items_with_totals():
    products_by_oem = build_products_by_oem()
    cart_data = load_cart_raw()

    cart_items = []
    subtotal = 0
    total_quantity = 0

    for item in cart_data.get("items", []):
        oem = item.get("oem")
        quantity = item.get("quantity", 1)

        product = products_by_oem.get(oem)
        if not product:
            continue

        price = product.get("price", 0)
        line_total = price * quantity

        subtotal += line_total
        total_quantity += quantity

        cart_items.append({
            "oem": oem,
            "quantity": quantity,
            "product": product,
            "line_total": line_total
        })

    return cart_items, subtotal, total_quantity


def update_cart_quantity(oem, quantity):
    cart_data = load_cart_raw()
    items = cart_data.get("items", [])

    found = False
    for item in items:
        if item.get("oem") == oem:
            item["quantity"] = quantity
            found = True
            break

    if not found:
        return False, "Item not found in cart", 404

    cart_data["items"] = items
    save_cart_raw(cart_data)
    return True, None, 200


def remove_from_cart(oem):
    cart_data = load_cart_raw()
    items = cart_data.get("items", [])

    new_items = [item for item in items if item.get("oem") != oem]

    if len(new_items) == len(items):
        return False, "Item not found", 404

    cart_data["items"] = new_items
    save_cart_raw(cart_data)
    return True, None, 200

def add_to_cart(oem, quantity=1):
    cart_data = load_cart_raw()
    items = cart_data.get("items", [])

    try:
        quantity = int(quantity)
    except (TypeError, ValueError):
        quantity = 1

    if quantity < 1:
        quantity = 1

    for item in items:
        if item.get("oem") == oem:
            item["quantity"] = item.get("quantity", 1) + quantity
            break
    else:
        items.append({"oem": oem, "quantity": quantity})

    cart_data["items"] = items
    save_cart_raw(cart_data)
    return True, None, 200
