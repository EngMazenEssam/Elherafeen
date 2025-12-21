from typing import Optional
from app.config import ADDRESSES_FILE
from app.utils.json_handler import JsonHandler


class AddressRepository:
    def __init__(self):
        self.json_handler = JsonHandler()

    def _load_addresses(self) -> dict:
        data = self.json_handler.read(ADDRESSES_FILE)
        return data if isinstance(data, dict) else {}

    def _save_addresses(self, addresses: dict) -> None:
        ADDRESSES_FILE.parent.mkdir(parents=True, exist_ok=True)
        self.json_handler.write(ADDRESSES_FILE, addresses)

    def get_by_email(self, email: str) -> Optional[dict]:
        email = email.lower().strip()
        addresses = self._load_addresses()
        return addresses.get(email)

    def update_address(
        self,
        email: str,
        street: str,
        city: str,
        country: str,
        phone: str
    ) -> bool:
        email = email.lower().strip()
        addresses = self._load_addresses()

        if email not in addresses:
            return False

        addresses[email] = {
            "street": street,
            "city": city,
            "country": country,
            "phone": phone
        }

        self._save_addresses(addresses)
        return True
