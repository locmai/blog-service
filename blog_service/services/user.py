from datetime import datetime, timedelta

import jwt
from bson.objectid import ObjectId
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt import PyJWTError
from passlib.context import CryptContext

from blog_service.core.config import (ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM,
                                      SECRET_KEY)
from blog_service.core.database import get_repository
from blog_service.models.query import QueryModel
from blog_service.models.token import TokenData
from blog_service.models.user import User, UserInDB
from blog_service.repositories.user import UserRepository
from blog_service.services.base import BaseService, HealthService


class UserService(BaseService, HealthService):
    def __init__(self, repo: UserRepository = Depends(get_repository(UserRepository))):
        super().__init__(repo)

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    async def get_user(self, username: str):
        user = await self.repo.find_one({'username': username})
        if user != None:
            return UserInDB(**user)

    async def get_user_by_id(self, user_id: str):
        user = await self.repo.find_one({'_id': ObjectId(user_id)})
        if user != None:
            return UserInDB(**user)

    async def authenticate_user(self, username: str, password: str):
        user = await self.get_user(username)
        if not user:
            return False
        if not self.verify_password(password, user.hashed_password):
            return False
        return user

    async def create_access_token(self, *, data: dict, expires_delta: timedelta = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, str(SECRET_KEY), ALGORITHM)
        return encoded_jwt

    async def get_current_user(self, token: str = Depends(oauth2_scheme)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
            token_data = TokenData(username=username)
        except PyJWTError:
            raise credentials_exception
        user = await self.get_user(username=token_data.username)
        if user is None:
            raise credentials_exception
        return user

    async def get_current_active_user(self, current_user: User = Depends(get_current_user)):
        if current_user.active:
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user
