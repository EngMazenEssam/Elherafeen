from app.config import DATA_DIR
from app.utils.json_handler import JsonHandler


class AdminRepository:
    def __init__(self):
        self.file = DATA_DIR / "admin.json"
        self.json_handler = JsonHandler()

    def get_all(self):
        data = self.json_handler.read(self.file)
        return data if isinstance(data, list) else []

    def find_by_email(self, email):
        email = (email or "").lower().strip()
        for admin in self.get_all():
            if admin.get("email", "").lower().strip() == email:
                return admin
        return None
