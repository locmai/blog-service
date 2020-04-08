from .base import DBModelMixin
from pydantic import BaseModel


class Token(DBModelMixin):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str = None
