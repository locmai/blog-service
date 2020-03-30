from fastapi import Depends

from blog_service.core.database import get_repository
from blog_service.models.article import Article
from blog_service.models.query import QueryModel
from blog_service.repositories.article import ArticleRepository
from blog_service.services.base import BaseService, HealthService

from typing import Callable

class ArticleService(BaseService, HealthService):
    def __init__(self, repo: ArticleRepository = Depends(get_repository(ArticleRepository))):
        super().__init__(repo)