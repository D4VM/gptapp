from fastapi import HTTPException, status

from app.database import engine
from app.users.models import UserModel
from app.users.schemas import SUserRequest, SUserAuth
from app.users.auth import get_password_hash, verify_password


class UserService:

    @classmethod
    def add_new_user(cls, user: SUserRequest):
        user_model = UserModel(name=user.name, email=user.email, password=user.password)
        # Check if the user already exists
        existing_user = engine.find_one(UserModel, UserModel.email == user_model.email)
        if existing_user:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")

        # Save the user to the database
        saved_user = engine.save(user_model)
        return saved_user

    @classmethod
    def get_user_by_id(cls, user_id):
        existing_user = engine.find_one(UserModel, UserModel.id == user_id)
        if not existing_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return existing_user

    @classmethod
    def authenticate_user(cls, user: SUserAuth):
        existing_user = engine.find_one(UserModel, UserModel.email == user.email)
        if not verify_password(user.password, existing_user.hashed_password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        return existing_user
