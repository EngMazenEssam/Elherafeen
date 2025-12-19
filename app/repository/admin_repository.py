import json
from app.config import DATA_DIR

class AdminRepository:
    def __init__(self):
        self.file = DATA_DIR / "admins.json"

    def find_by_email(self, email):
        if not self.file.exists():
            return None
        with open(self.file, "r", encoding="utf-8") as f:
            data = json.load(f)
        return next((a for a in data if a["email"] == email), None)
