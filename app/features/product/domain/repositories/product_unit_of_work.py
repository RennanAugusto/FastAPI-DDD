from abc import abstractmethod

from app.core.unit_of_work.unit_of_work import AbstractUnitOfWork
from app.features.product.domain.repositories.product_repository import ProductRepository


class ProductUnitOfWork(AbstractUnitOfWork):

    @abstractmethod
    def get_product_repository(self) -> ProductRepository:
        raise NotImplementedError()