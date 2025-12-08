import hashlib
from typing import Optional
from app.models.user import User
from app.repository.user_repository import UserRepository


class UserService:

    def __init__(self, repo: Optional[UserRepository] = None) -> None:
        self.repo = repo or UserRepository()

    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def _check_password(self, plain: str, hashed: str) -> bool:
        return self._hash_password(plain) == hashed

    def register_user(
        self,
        fullname: str,
        email: str,
        phone: str,
        password: str,
        confirm: str,
    ) -> User:
        fullname = (fullname or "").strip()
        email = (email or "").strip().lower()
        phone = (phone or "").strip()

        if not fullname or not email or not password or not confirm:
            raise ValueError("Please fill all required fields.")

        if password != confirm:
            raise ValueError("Passwords do not match.")

        if self.repo.find_by_email(email):
            raise ValueError("This email is already registered.")

        password_hash = self._hash_password(password)
        new_user = User.create(
            fullname=fullname,
            email=email,
            phone=phone,
            password_hash=password_hash,
        )
        self.repo.add_user(new_user)
        return new_user

    def login_user(self, email: str, password: str) -> User:
        email = (email or "").strip().lower()
        if not email or not password:
            raise ValueError("Email and password are required.")

        user = self.repo.find_by_email(email)
        if not user:
            raise ValueError("Invalid email or password.")

        if not self._check_password(password, user.password_hash):
            raise ValueError("Invalid email or password.")

        return user
