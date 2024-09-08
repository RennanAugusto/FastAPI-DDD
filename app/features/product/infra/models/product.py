from datetime import datetime
from sqlalchemy import Float, Column, String, Integer, TIMESTAMP
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func
from automapper import mapper
from app.features.product.domain.entities.product_entity import ProductEntity


Base = declarative_base()
metadata = Base.metadata

class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    title = Column(String(25))
    description = Column(String(225))
    price = Column(Float(precision=2))

    def to_entity(self) -> 'ProductEntity':
        return mapper.to(ProductEntity).map(self)

    @staticmethod
    def to_model(product: 'ProductEntity') -> 'Product':
        return Product(
            id=product.id,
            created_at=product.created_at,
            title=product.title,
            description=product.description,
            price=product.price
        )