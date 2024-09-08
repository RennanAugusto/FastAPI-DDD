from abc import ABC, abstractmethod

from typing import Sequence

from app.features.product.domain.DTO.product_dto import ProductSchema, PostProductSchema, PutProductSchema
from app.features.product.domain.entities.product_entity import ProductEntity
from app.features.product.domain.repositories.product_unit_of_work import ProductUnitOfWork
from app.features.product.infra.models.product import Product


class ProductService(ABC):

    @abstractmethod
    def get_product_by_id(self, product_id: int) -> ProductSchema:
        raise NotImplementedError()

    @abstractmethod
    def get_all_products(self) -> Sequence[ProductSchema]:
        raise NotImplementedError()

    @abstractmethod
    def update_product(self, product_entity: PutProductSchema) -> ProductSchema | None:
        raise NotImplementedError()

    @abstractmethod
    def create_product(self, product: PostProductSchema) -> ProductSchema:
        raise NotImplementedError()

    @abstractmethod
    def delete_product(self, product_id: int) -> None:
        raise NotImplementedError()

    @abstractmethod
    def get_products_by_price_between(self, price_start: float, price_end: float) -> Sequence[ProductSchema]:
        raise NotImplementedError()


class ProductServiceImpl(ProductService):

    def __init__(self, unit_of_work: ProductUnitOfWork):
        self._unit_of_work = unit_of_work

    def get_product_by_id(self, product_id: int) -> ProductSchema:
        return ProductSchema.from_entity(self._unit_of_work.get_product_repository().get_by_id(product_id))

    def get_all_products(self) -> Sequence[ProductSchema]:
        result = self._unit_of_work.get_product_repository().get_all()
        return [ProductSchema.from_entity(product) for product in result]

    def update_product(self, product: PutProductSchema) -> ProductSchema | None:
        product_entity = PutProductSchema.to_entity(product)
        try:
            self._unit_of_work.begin_transaction()
            result: ProductEntity = self._unit_of_work.get_product_repository().update(product_entity)
            self._unit_of_work.commit_transaction()
        except Exception as e:
            self._unit_of_work.rollback_transaction()
            raise e

        if result:
            return ProductSchema.from_entity(result)
        else:
            return None

    def create_product(self, product: PostProductSchema) -> ProductSchema:
        product_entity = PostProductSchema.to_entity(product)
        try:
            self._unit_of_work.begin_transaction()
            result: ProductEntity = self._unit_of_work.get_product_repository().insert(product_entity)
            self._unit_of_work.commit_transaction()
        except Exception as e:
            self._unit_of_work.rollback_transaction()
            raise e

        return ProductSchema.from_entity(result)

    def delete_product(self, product_id: int) -> None:
        try:
            self._unit_of_work.begin_transaction()
            self._unit_of_work.get_product_repository().delete(product_id)
            self._unit_of_work.commit_transaction()
        except Exception as e:
            self._unit_of_work.rollback_transaction()
            raise e

    def get_products_by_price_between(self, price_start: float, price_end: float) -> Sequence[ProductSchema]:
        result = self._unit_of_work.get_product_repository().get_by_price_between(price_start, price_end)
        return [ProductSchema.from_entity(product) for product in result]