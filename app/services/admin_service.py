import hashlib
from app.repository.admin_repository import AdminRepository


class AdminService:
    def __init__(self):
        self.repo = AdminRepository()

    def login(self, email, password):
        email = (email or "").lower().strip()
        password = password or ""

        if not email or not password:
            raise ValueError("Email and password are required")

        admin = self.repo.find_by_email(email)
        if not admin:
            raise ValueError("Invalid email or password")

        hashed = hashlib.sha256(password.encode("utf-8")).hexdigest()
        print("INPUT HASH:", hashed)
        print("FILE HASH:", admin.get("password_hash"))


        if admin.get("password_hash") != hashed:
            raise ValueError("Invalid email or password")

        return admin
