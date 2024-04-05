from odmantic import ObjectId
from pydantic import BaseModel, EmailStr


class SUserRequest(BaseModel):
    name: str
    email: EmailStr
    password: str


class SUserResponse(BaseModel):
    id: ObjectId
    name: str
    email: EmailStr


class SUserSingle(BaseModel):
    user: SUserResponse


class SUserAuth(BaseModel):
    email: EmailStr
    password: str
