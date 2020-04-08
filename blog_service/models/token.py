from .base import DBModelMixin

class Token(DBModelMixin):
    access_token: str
    token_type: str


class TokenData(DBModelMixin):
    username: str = None