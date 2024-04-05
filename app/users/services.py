from fastapi import HTTPException, status

from app.database import engine
from app.users.models import Users
from app.users.schemas import SUserRequest, SUserAuth
from app.users.auth import get_password_hash, verify_password


class UserService:

    @classmethod
    def add_new_user(cls, data: SUserRequest):
        # Instantiate the model with the provided data
        user = Users(name=data.name, email=data.email, hashed_password=get_password_hash(data.password))

        # Check if the user already exists
        existing_user = engine.find_one(Users, Users.email == user.email)
        if existing_user:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")

        # Save the user to the database
        saved_user = engine.save(user)
        return saved_user

    @classmethod
    def get_user_by_id(cls, user_id):
        existing_user = engine.find_one(Users, Users.id == user_id)
        if not existing_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return existing_user

    @classmethod
    def authenticate_user(cls, user: SUserAuth):
        existing_user = engine.find_one(Users, Users.email == user.email)
        if not verify_password(user.password, existing_user.hashed_password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        return existing_user
