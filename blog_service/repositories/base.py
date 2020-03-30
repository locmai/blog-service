from typing import Any, List, Sequence, Tuple

from loguru import logger
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase, AsyncIOMotorCollection


def _log_query(query: str, query_params: Tuple[Any, ...]) -> None:
    logger.debug("query: {0}, values: {1}", query, query_params)


class BaseRepository:
    def __init__(self, database: AsyncIOMotorDatabase, name: str) -> None:
        self._database = database
        self._name = name

    @property
    def collection(self) -> AsyncIOMotorCollection:
        return self._database[self.name]

    @property
    def name(self) -> str:
        return self._name

    async def find(self, filter={}, limit=100):
        return await self.collection.find(filter).to_list(length=limit)

    async def find_one(self, filter={}):
        return await self.collection.find_one(filter)
