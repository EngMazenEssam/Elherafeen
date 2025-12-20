import json
import os
from typing import List, Dict, Any, Optional
from app.config import DATA_DIR  

PENDING_FILE = os.path.join(str(DATA_DIR), "pending.json")
APPROVED_FILE = os.path.join(str(DATA_DIR), "approved.json")

class SellerRepository:

    def _load_json(self, path: str) -> List[Dict[str, Any]]:
        if not os.path.exists(path):
            return []
        with open(path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                if isinstance(data, list):
                    return data
                return []
            except json.JSONDecodeError:
                return []

    def _save_json(self, path: str, data: List[Dict[str, Any]]) -> None:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def get_pending_products(self, seller_id: str = None) -> List[Dict[str, Any]]:
        products = self._load_json(PENDING_FILE)
        if seller_id:
            return [p for p in products if p.get("seller_id") == seller_id]
        return products

    def get_approved_products(self, seller_id: str = None) -> List[Dict[str, Any]]:
        products = self._load_json(APPROVED_FILE)
        if seller_id:
            return [p for p in products if p.get("seller_id") == seller_id]
        return products

    def add_pending_product(self, product: Dict[str, Any]) -> None:
        products = self._load_json(PENDING_FILE)
        products.append(product)
        self._save_json(PENDING_FILE, products)

    def move_to_approved(self, product_id: str) -> bool:
        pending = self._load_json(PENDING_FILE)
        product_to_approve = None
        new_pending = []
        
        for p in pending:
            if p.get("id") == product_id:
                product_to_approve = p
            else:
                new_pending.append(p)
        
        if product_to_approve:
            self._save_json(PENDING_FILE, new_pending)
            
            approved = self._load_json(APPROVED_FILE)
            product_to_approve["status"] = "Approved"
            approved.append(product_to_approve)
            self._save_json(APPROVED_FILE, approved)
            return True
        return False
