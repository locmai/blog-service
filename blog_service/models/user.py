from .base import DBModelMixin

class User(DBModelMixin):
    username: str
    email: str = None
    full_name: str = None
    active: bool = None


class UserInDB(User):
    hashed_password: str