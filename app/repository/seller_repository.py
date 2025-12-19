import json
from typing import Optional
from app.config import DATA_DIR


class SellerRepository:
    def __init__(self):
        self.file = DATA_DIR / "sellers.json"

    def _load(self):
        if not self.file.exists():
            return []
        with self.file.open("r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
        return data if isinstance(data, list) else []

    def _save(self, data):
        self.file.parent.mkdir(parents=True, exist_ok=True)
        with self.file.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def find_by_email(self, email: str) -> Optional[dict]:
        email = email.lower().strip()
        for seller in self._load():
            if seller.get("email", "").lower().strip() == email:
                return seller
        return None

    def add(self, seller: dict) -> dict:
        data = self._load()
        data.append(seller)
        self._save(data)
        return seller
