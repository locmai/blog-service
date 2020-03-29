from fastapi import APIRouter, Depends
from blog_service.repositories.article import ArticleRepository
from blog_service.core.database import get_repository
from loguru import logger
from blog_service.models.article import Article
from fastapi.encoders import jsonable_encoder
from blog_service.models.query import QueryModel

import json

router = APIRouter()

@router.get("/articles")
async def get_articles(article_repo: ArticleRepository = Depends(get_repository(ArticleRepository))):

    articles = await article_repo.get_articles()

    article_results = []
    for article in articles:
        article_results.append(Article(**article))

    return article_results

@router.post("/articles")
async def query_articles(query: QueryModel, article_repo: ArticleRepository = Depends(get_repository(ArticleRepository))):
    articles = await article_repo.get_articles_by_filter(query.filter)
    
    article_results = []
    for article in articles:
        article_results.append(Article(**article))

    return article_results
