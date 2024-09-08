from sqlalchemy.orm import Session

from fastapi import Depends

from app.core.database.database import get_session
from app.features.product.domain.repositories.product_repository import ProductRepository
from app.features.product.domain.repositories.product_unit_of_work import ProductUnitOfWork
from app.features.product.domain.services.product_service import ProductService, ProductServiceImpl
from app.features.product.infra.repositories.product_repository_impl import ProductRepositoryImpl
from app.features.product.infra.repositories.product_unit_of_work_impl import ProductUnitOfWorkImpl


def get_product_repository(session: Session = Depends(get_session)) -> ProductRepository:
    return ProductRepositoryImpl(session)

def get_unit_of_work(session: Session = Depends(get_session), product_repository: ProductRepository = Depends(get_product_repository)) -> ProductUnitOfWork:
    return ProductUnitOfWorkImpl(session, product_repository)

def get_product_service(unit_of_work: ProductUnitOfWork = Depends(get_unit_of_work)) -> ProductService:
    return ProductServiceImpl(unit_of_work)