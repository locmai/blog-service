from typing import Type
from blog_service.repositories.base import BaseRepository
from typing import Callable

class BaseService:
    def __init__(self, repo: Type[BaseRepository]):
        self._repo = repo

    @property
    def repo(self) -> Type[BaseRepository]:
        return self._repo

    async def get(self,filter = {}):
        return await self.repo.find(filter)

    async def getOne(self,filter = {}):
        return await self.repo.find_one(filter)

class HealthService:
    pass
