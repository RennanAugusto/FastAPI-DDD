from datetime import datetime


class ProductEntity:
    id: int | None = None
    created_at: datetime | None = None
    title: str
    description: str
    price: float

    def __init__(self, id: int | None, created_at: datetime | None, title: str, description: str, price: float):
        self.id = id
        self.created_at = created_at
        self.title = title
        self.description = description
        self.price = price