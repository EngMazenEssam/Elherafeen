import os
import json

ROOT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

DATA_FOLDER = os.path.join(ROOT_DIR, "data")

CART_JSON_PATH = os.path.join(DATA_FOLDER, "cart.json")


def read_json_file(path, default_value):

    if not os.path.exists(path):
        return default_value

    with open(path, encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return default_value

def write_json_file(path, data):

    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_cart_raw():

    return read_json_file(CART_JSON_PATH, default_value={"items": []})


def save_cart_raw(cart_dictionary):

    write_json_file(CART_JSON_PATH, cart_dictionary)
