from odmantic import ObjectId
from pydantic import BaseModel


class SProduct(BaseModel):
    category: str
    title: str
    description: str
    price: float
    stock: int
    published: bool
