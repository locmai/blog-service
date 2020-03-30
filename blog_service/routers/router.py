from fastapi import APIRouter
from .article import router as article_router
from loguru import logger
router = APIRouter()

router.include_router(article_router)
