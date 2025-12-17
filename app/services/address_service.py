import json
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA_DIR = os.path.join(BASE_DIR, "data")
ADDRESS_FILE = os.path.join(DATA_DIR, "addresses.json")


def get_address_for_user(email):
    if not os.path.exists(ADDRESS_FILE):
        return None

    with open(ADDRESS_FILE, encoding="utf-8") as f:
        data = json.load(f)

    return data.get(email)
