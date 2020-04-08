from fastapi import APIRouter
from .article import router as article_router
from .user import router as user_router
from loguru import logger

@logger.catch
def get_router():
    router = APIRouter()
    router.include_router(article_router,prefix='/articles')
    router.include_router(user_router,prefix='/users')
    return router
