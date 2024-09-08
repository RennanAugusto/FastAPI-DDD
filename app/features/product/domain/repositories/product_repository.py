from abc import abstractmethod
from typing import List

from app.core.repositories.base_repository import BaseRepository
from app.features.product.domain.entities.product_entity import ProductEntity


class ProductRepository(BaseRepository[ProductEntity]):

    @abstractmethod
    def get_by_price_between(self, price_start: float, price_end: float) -> List[ProductEntity]:
        raise NotImplementedError()