import json
from app.config import DATA_DIR

class ApprovedRepository:
    def __init__(self):
        self.file = DATA_DIR / "products.json"

    def add(self, product):
        data = []
        if self.file.exists():
            with open(self.file, "r", encoding="utf-8") as f:
                data = json.load(f)

        data.append(product)

        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
