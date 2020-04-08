from fastapi import APIRouter, Depends

from blog_service.repositories.article import ArticleRepository
from blog_service.core.database import get_repository
from loguru import logger
from blog_service.models.article import Article
from fastapi.encoders import jsonable_encoder
from blog_service.models.query import QueryModel
from blog_service.services.article import ArticleService

import json

router = APIRouter()

from typing import List
@router.get('/', response_model=List[Article])
async def get_articles(article_svc: ArticleService = Depends(ArticleService)):
    articles = await article_svc.get()

    article_results = []
    for article in articles:
        article_results.append(Article(**article))

    # TODO: Update response_model to ArticleListResponse later
    return article_results
