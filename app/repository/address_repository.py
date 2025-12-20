import json
from typing import Optional
from app.config import ADDRESSES_FILE


class AddressRepository:

    def _load_addresses(self) -> dict:
        if not ADDRESSES_FILE.exists():
            return {}

        with ADDRESSES_FILE.open("r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}

        return data if isinstance(data, dict) else {}

    def _save_addresses(self, addresses: dict) -> None:
        ADDRESSES_FILE.parent.mkdir(parents=True, exist_ok=True)
        with ADDRESSES_FILE.open("w", encoding="utf-8") as f:
            json.dump(addresses, f, indent=2, ensure_ascii=False)

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
