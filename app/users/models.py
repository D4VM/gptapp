from odmantic import Field, Model
from pydantic import EmailStr


class Users(Model):
    name: str
    email: EmailStr = Field(unique=True)
    hashed_password: str
