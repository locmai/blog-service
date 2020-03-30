from fastapi import APIRouter
from .article import router as article_router
from loguru import logger

@logger.catch
def get_router():
    router = APIRouter()
    router.include_router(article_router,prefix='/article')
    return router
