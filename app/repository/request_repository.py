import json
from app.config import DATA_DIR

class RequestRepository:
    def __init__(self):
        self.file = DATA_DIR / "request.json"

    def get_all(self):
        if not self.file.exists():
            return []
        with open(self.file, "r", encoding="utf-8") as f:
            return json.load(f)

    def remove_by_id(self, request_id):
        data = self.get_all()
        item = next((r for r in data if r["id"] == request_id), None)
        if not item:
            return None
        data.remove(item)
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return item
