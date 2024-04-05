from odmantic import Field, Model
from pydantic import EmailStr


class UserModel(Model):
    name: str
    email: EmailStr = Field(unique=True)
    password: str
