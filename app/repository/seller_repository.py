import json
from typing import List, Dict, Any, Optional
from app.config import DATA_DIR
from pathlib import Path


class SellerRepository:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SellerRepository, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.pending_file = DATA_DIR / "pending.json"
        self.approved_file = DATA_DIR / "approved.json"
        self.seller_file = DATA_DIR / "sellers.json"

    def _load_json(self, path: Path) -> List[Dict[str, Any]]:
        if not path.exists():
            return []
        with path.open("r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
        return data if isinstance(data, list) else []

    def _save_json(self, path: Path, data: List[Dict[str, Any]]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def get_pending_products(self, seller_id: str = None) -> List[Dict[str, Any]]:
        products = self._load_json(self.pending_file)
        if seller_id:
            return [p for p in products if p.get("seller_id") == seller_id]
        return products

    def get_approved_products(self, seller_id: str = None) -> List[Dict[str, Any]]:
        products = self._load_json(self.approved_file)
        if seller_id:
            return [p for p in products if p.get("seller_id") == seller_id]
        return products

    def add_pending_product(self, product: Dict[str, Any]) -> None:
        products = self._load_json(self.pending_file)
        products.append(product)
        self._save_json(self.pending_file, products)

    def move_to_approved(self, product_id: str) -> bool:
        pending = self._load_json(self.pending_file)
        product_to_approve = None
        new_pending = []

        for p in pending:
            if p.get("id") == product_id:
                product_to_approve = p
            else:
                new_pending.append(p)

        if product_to_approve:
            self._save_json(self.pending_file, new_pending)

            approved = self._load_json(self.approved_file)
            product_to_approve["status"] = "Approved"
            approved.append(product_to_approve)
            self._save_json(self.approved_file, approved)
            return True
        return False

    def find_by_email(self, email: str) -> Optional[dict]:
        email = email.lower().strip()
        for seller in self._load_json(self.seller_file):
            if seller.get("email", "").lower().strip() == email:
                return seller
        return None

    def add(self, seller: dict) -> dict:
        data = self._load_json(self.seller_file)
        data.append(seller)
        self._save_json(self.seller_file, data)
        return seller
