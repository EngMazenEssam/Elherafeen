import json
from app.config import DATA_DIR


class ProductModerationRepository:
    def __init__(self):
        self.pending_file = DATA_DIR / "pending.json"
        self.approved_file = DATA_DIR / "approved.json"

    def _read(self, file):
        if not file.exists():
            return []
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)

    def _write(self, file, data):
        with open(file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def get_pending(self):
        return self._read(self.pending_file)

    def approve(self, product_id):
        pending = self._read(self.pending_file)
        approved = self._read(self.approved_file)

        for product in pending:
            if product["id"] == product_id:
                approved.append(product)
                pending.remove(product)
                self._write(self.pending_file, pending)
                self._write(self.approved_file, approved)
                return

        raise ValueError("Product not found")

    def reject(self, product_id):
        pending = self._read(self.pending_file)

        for product in pending:
            if product["id"] == product_id:
                pending.remove(product)
                self._write(self.pending_file, pending)
                return

        raise ValueError("Product not found")
