from fastapi import FastAPI
from app.config import Settings

from app.features.product.application.routes.product_router import router as product_router

if __name__ == 'main':
    app = FastAPI()

    app.include_router(product_router)