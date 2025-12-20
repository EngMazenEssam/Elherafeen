import json
from app.config import DATA_DIR


class AdminRepository:
    def __init__(self):
        self.file = DATA_DIR / "admin.json"

    def get_all(self):
        if not self.file.exists():
            return []
        with open(self.file, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                return []
        return data if isinstance(data, list) else []

    def find_by_email(self, email):
        email = (email or "").lower().strip()
        for admin in self.get_all():
            if admin.get("email", "").lower().strip() == email:
                return admin
        return None
