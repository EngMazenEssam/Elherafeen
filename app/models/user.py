from dataclasses import dataclass, asdict
from typing import Optional
import uuid


@dataclass
class User:
    id: str
    fullname: str
    email: str
    phone: Optional[str]
    password_hash: str

    @staticmethod
    def create(fullname: str, email: str, phone: str, password_hash: str) -> "User":
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
