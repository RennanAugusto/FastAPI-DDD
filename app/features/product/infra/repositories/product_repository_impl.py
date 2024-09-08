from typing import List, Sequence

from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete, MetaData, Table

from app.core.repositories.base_repository import T
from app.features.product.domain.entities.product_entity import ProductEntity
from app.features.product.domain.repositories.product_repository import ProductRepository
from app.features.product.infra.models.product import Product


class ProductRepositoryImpl(ProductRepository):

    def __init__(self, session: Session):
        self.session = session

    def delete(self, entity_id: int):
        statement = delete(Product).filter_by(id=entity_id)
        self.session.execute(statement)

    def get_all(self) -> Sequence[ProductEntity]:
        statement = select(Product)
        try:
            result: Sequence[Product] = self.session.execute(statement).scalars().all()
        except NoResultFound:
            return []

        return [product.to_entity() for product in result]

    def get_by_id(self, entity_id: int) -> ProductEntity | None:
        statement = select(Product).filter_by(id=entity_id)
        result: Product | None = self.session.execute(statement).scalars().first()
        if result is None:
            return None

        return result.to_entity()


    def update(self, entity: ProductEntity) -> ProductEntity | None:
        product = Product.to_model(entity)
        update_data: dict = {k: v for k, v in vars(product).items() if k not in ['id', 'created_at', '_sa_instance_state']}
        statement = update(Product).where(Product.id == product.id).values(update_data).returning(Product)
        print(statement)
        result = self.session.execute(statement)
        update_product = result.scalar_one_or_none()

        if update_product:
            return update_product.to_entity()
        else:
            return None

    def insert(self, entity: ProductEntity) -> ProductEntity:
        product: Product = Product.to_model(entity)
        self.session.add(product)
        self.session.flush()

        return product.to_entity()

    def get_by_price_between(self, price_start: float, price_end: float) -> Sequence[ProductEntity]:
        statement = select(Product).filter(Product.price >= price_start, Product.price <= price_end)
        try:
            result: Sequence[Product] = self.session.execute(statement).scalars().all()
        except NoResultFound:
            return []

        return [product.to_entity() for product in result]
