from typing import List, Optional

from .base import DBModelMixin, ObjectIdStr
from pydantic import Field


class ArticleBase(DBModelMixin):
    title: str
    description: str
    body: str
    tags: List[str]


class Article(ArticleBase):
    author_id: Optional[ObjectIdStr]
    like_count: int


class ArticleInDb(Article):
    pass


class CRUDArticle(ArticleBase):
    author_id: Optional[ObjectIdStr]
    like_count: int


class ArticleResponse(DBModelMixin):
    articles: List[Article]


class ManyArticleResponse(DBModelMixin):
    articles: List[Article]
    articles_count: int = Field(..., alias="articlesCount")
