from blog_service.repositories.base import BaseRepository
from motor.motor_asyncio import AsyncIOMotorClient,AsyncIOMotorDatabase
from blog_service.core.constants import ARTICLE_COLLECTION


class ArticleRepository(BaseRepository):
    def __init__(self, database: AsyncIOMotorDatabase) -> None:
        super().__init__(database, name=ARTICLE_COLLECTION)

    async def create_article(self,title,description,authorId, tagId):
        return None

    async def get_articles(self):
        return await self.get_articles_by_filter()

    async def get_articles_by_filter(self, filter = {}):
        return await self.collection.find(filter).to_list(length=100)

    async def find_one(self, filter):
        return await self.collection.find(filter).to_list(length=1)