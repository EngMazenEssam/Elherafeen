from dataclasses import dataclass, asdict
from typing import Optional
import uuid


@dataclass
class User:
    """تمثيل المستخدم في النظام."""
    id: str
    fullname: str
    email: str
    phone: Optional[str]
    password_hash: str

    @staticmethod
    def create(fullname: str, email: str, phone: str, password_hash: str) -> "User":
        """factory لإنشاء يوزر جديد بـ id فريد"""
        return User(
            id=str(uuid.uuid4()),
            fullname=fullname,
            email=email.lower().strip(),
            phone=phone.strip() if phone else "",
            password_hash=password_hash,
        )

    def to_dict(self) -> dict:
        return asdict(self)

    @staticmethod
    def from_dict(data: dict) -> "User":
        return User(
            id=data["id"],
            fullname=data["fullname"],
            email=data["email"],
            phone=data.get("phone", ""),
            password_hash=data["password_hash"],
        )
