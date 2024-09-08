from sqlalchemy.orm import Session

from app.core.unit_of_work.unit_of_wortk_impl import UnitOfWorkImpl
from app.features.product.domain.repositories.product_repository import ProductRepository
from app.features.product.domain.repositories.product_unit_of_work import ProductUnitOfWork


class ProductUnitOfWorkImpl(UnitOfWorkImpl, ProductUnitOfWork):

    def __init__(self, session: Session, product_repository: ProductRepository):
        super().__init__(session)
        self._product_repository = product_repository

    def get_product_repository(self) -> ProductRepository:
        return self._product_repository