from fastapi import APIRouter
from app.products.schemas import SProduct

router = APIRouter(
    prefix='/products',
    tags=['Products']
)


@router.get('', response_model=SProduct)
def get_all_products():
    pass
