from dataclasses import dataclass

@dataclass
class ProductRequest:
    id: str
    seller_id: str
    title: str
    category: str
    price: float
    image: str
    status: str = "pending"
