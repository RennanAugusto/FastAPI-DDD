from fastapi import APIRouter, Depends, Path
from starlette import status
from typing import Sequence

from app.features.product.dependencies import get_product_service
from app.features.product.domain.DTO.product_dto import ProductSchema, PostProductSchema, PutProductSchema
from app.features.product.domain.services.product_service import ProductService

#product_service: ProductService = Depends(get_product_service)
router = APIRouter(prefix="/products", tags=["products"])

@router.get("/{product_id}")
async def get_product(product_id: int, product_service: ProductService = Depends(get_product_service)) -> ProductSchema:
    return product_service.get_product_by_id(product_id)

@router.get("", response_model=Sequence[ProductSchema], status_code=status.HTTP_200_OK)
async def get_products(product_service: ProductService = Depends(get_product_service)):
    return product_service.get_all_products()

@router.post("", status_code=status.HTTP_201_CREATED)
async def post_product(body: PostProductSchema, product_service: ProductService = Depends(get_product_service)) -> ProductSchema:
    return product_service.create_product(body)

@router.put("")
async def post_product(body: PutProductSchema, product_service: ProductService = Depends(get_product_service)) -> ProductSchema:
    return product_service.update_product(body)

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: int, product_service: ProductService = Depends(get_product_service)) -> None:
    product_service.delete_product(product_id)

@router.get("/{price_start}/{price_end}", response_model=Sequence[ProductSchema], status_code=status.HTTP_200_OK)
async def get_by_price_between(price_start: float, price_end: float, product_service: ProductService = Depends(get_product_service)):
    return product_service.get_products_by_price_between(price_start, price_end)