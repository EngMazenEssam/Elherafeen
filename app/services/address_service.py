from typing import Optional
from app.repository.address_repository import AddressRepository



class AddressService:
    def __init__(self, repo: Optional[AddressRepository] = None):
        self.repo = repo or AddressRepository()

    def get_address_for_user(self, email: str) -> Optional[dict]:
        return self.repo.get_by_email(email)

    def update_address(
        self,
        email: str,
        street: str,
        city: str,
        country: str,
        phone: str
    ) -> bool:
        return self.repo.update_address(
            email=email,
            street=street,
            city=city,
            country=country,
            phone=phone
        )
