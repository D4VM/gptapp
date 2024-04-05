from fastapi import APIRouter

from app.orders.schemas import SOrder


router = APIRouter(
    prefix='/orders',
    tags=['Order']

)


@router.get('', response_model=SOrder)
def get_all_orders():
    pass
