from fastapi import APIRouter

from odmantic import ObjectId

from app.users.schemas import *
from app.users.services import UserService

router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.post('/add', response_model=SUserSingle)
def add_new_user(user: SUserRequest):
    user = UserService.add_new_user(user)
    return {"user": user}


@router.post('/auth', response_model=SUserSingle)
def authenticate_user(user: SUserAuth):
    authenticated = UserService.authenticate_user(user)
    return {"user": authenticated}


@router.get('/{user_id}', response_model=SUserSingle)
def get_user_by_id(user_id: ObjectId):
    user = UserService.get_user_by_id(user_id)
    return {"user": user}
