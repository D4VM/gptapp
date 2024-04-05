from odmantic import ObjectId
from pydantic import BaseModel


class SOrder(BaseModel):
    id: ObjectId
    user_id: ObjectId
    products_id: list[ObjectId]
    total_cost: float
    status: str
