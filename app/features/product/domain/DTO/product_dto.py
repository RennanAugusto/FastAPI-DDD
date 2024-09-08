from datetime import datetime
from typing import Optional

from automapper import mapper
from pydantic import BaseModel, Field

from app.features.product.domain.entities.product_entity import ProductEntity

class ProductSchema(BaseModel):
    id: int
    created_at: datetime
    title: str
    description: str
    price: float

    @staticmethod
    def to_entity(product: 'ProductSchema') -> ProductEntity:
        return ProductEntity(
            id = product.id,
            created_at = product.created_at,
            title = product.title,
            description = product.description,
            price = product.price
        )

    @staticmethod
    def from_entity(product_entity: ProductEntity) -> 'ProductSchema':
        if product_entity is None:
            return None

        return ProductSchema.new(
            id = product_entity.id,
            created_at = product_entity.created_at,
            title = product_entity.title,
            description = product_entity.description,
            price = product_entity.price
        )

    @classmethod
    def new(cls, id: int, created_at: datetime, title: str, description: str, price: float):
        return cls(id=id, created_at=created_at, title=title, description=description, price=price)


class PostProductSchema(BaseModel):
    title: str
    description: str
    price: float

    @staticmethod
    def to_entity(product: 'PostProductSchema') -> ProductEntity:
        return ProductEntity(
            id = None,
            created_at = None,
            title = product.title,
            description = product.description,
            price = product.price
        )

class PutProductSchema(BaseModel):
    id: int
    title: str
    description: str
    price: float

    @staticmethod
    def to_entity(product: 'PutProductSchema') -> ProductEntity:
        return ProductEntity(
            id = product.id,
            created_at = None,
            title = product.title,
            description = product.description,
            price = product.price
        )