from fastapi import HTTPException, status

from app.database import engine
from app.products.models import ProductModel
from app.products.schemas import SProduct


class ProductService:

    @classmethod
    def add_one_product(cls, product: ProductModel):

        data = engine.save(product)
        return data
