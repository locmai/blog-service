from blog_service.repositories.base import BaseRepository
from motor.motor_asyncio import AsyncIOMotorClient,AsyncIOMotorDatabase
from blog_service.core.constants import ARTICLE_COLLECTION


class ArticleRepository(BaseRepository):
    def __init__(self, database: AsyncIOMotorDatabase) -> None:
        super().__init__(database, name=ARTICLE_COLLECTION)