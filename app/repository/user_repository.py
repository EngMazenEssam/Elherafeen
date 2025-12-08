import json
from typing import List, Optional
from app.config import USERS_FILE
from app.models.user import User


class UserRepository:

    def _load_users(self) -> List[dict]:
        if not USERS_FILE.exists():
            return []
        with USERS_FILE.open("r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
        if not isinstance(data, list):
            return []
        return data

    def _save_users(self, users: List[dict]) -> None:
        USERS_FILE.parent.mkdir(parents=True, exist_ok=True)
        with USERS_FILE.open("w", encoding="utf-8") as f:
            json.dump(users, f, ensure_ascii=False, indent=2)


    def get_all(self) -> List[User]:
        return [User.from_dict(u) for u in self._load_users()]

    def find_by_email(self, email: str) -> Optional[User]:
        email = email.lower().strip()
        for u in self._load_users():
            if u.get("email", "").lower().strip() == email:
                return User.from_dict(u)
        return None

    def add_user(self, user: User) -> User:
        users = self._load_users()
        users.append(user.to_dict())
        self._save_users(users)
        return user
