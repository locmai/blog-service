from blog_service.repositories.base import BaseRepository
from motor.motor_asyncio import AsyncIOMotorClient,AsyncIOMotorDatabase
from blog_service.core.constants import USER_COLLECTION


class UserRepository(BaseRepository):
    def __init__(self, database: AsyncIOMotorDatabase) -> None:
        super().__init__(database, name=USER_COLLECTION)