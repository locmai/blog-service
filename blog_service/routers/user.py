import json
from datetime import datetime, timedelta

import jwt
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from loguru import logger

from blog_service.core.config import (ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM,
                                      SECRET_KEY)
from blog_service.core.database import get_repository
from blog_service.models.query import QueryModel
from blog_service.models.token import Token
from blog_service.models.user import User
from blog_service.services.user import UserService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/users/token")

router = APIRouter()


@router.get('/{username}')
async def get_user_by_username(username: str, user_svc: UserService = Depends(UserService)):
    return await user_svc.get_user(username)


@router.get('/id/{user_id}', response_model=User)
async def get_user_by_id(user_id: str, user_svc: UserService = Depends(UserService)):
    return await user_svc.get_user_by_id(user_id)


@router.get("/me/", response_model=User)
async def get_current_logged_in_user(user_svc: UserService = Depends(UserService), token: str = Depends(oauth2_scheme)):
    return await user_svc.get_current_user(token)


@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), user_svc: UserService = Depends(UserService)):
    user = await user_svc.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = await user_svc.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
