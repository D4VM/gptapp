from fastapi import APIRouter
from app.products.models import ProductModel
from app.products.services import ProductService
router = APIRouter(
    prefix='/products',
    tags=['Products']
)


@router.post('/add')
def add_product(product: ProductModel):
    pr = ProductService.add_one_product(product)
    return pr