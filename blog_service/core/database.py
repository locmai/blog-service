from typing import AsyncGenerator, Callable, Type

from fastapi import Depends, FastAPI
from loguru import logger
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.requests import Request

from blog_service.core.config import (DATABASE_URL, MAX_CONNECTIONS,
                                      MIN_CONNECTIONS)
from blog_service.repositories.base import BaseRepository


async def connect_to_db(app: FastAPI) -> None:
    logger.info("Connecting to {0}", repr(DATABASE_URL))

    app.state.client = AsyncIOMotorClient(
        DATABASE_URL, maxPoolSize=MAX_CONNECTIONS, minPoolSize=MIN_CONNECTIONS)

    logger.info("Connection established")


async def close_db_connection(app: FastAPI) -> None:
    logger.info("Closing connection to database")

    app.state.client.close()

    logger.info("Connection closed")


def _get_client(request: Request) -> AsyncIOMotorClient:
    return request.app.state.client


def get_repository(repo: Type[BaseRepository]) -> Callable:  # type: ignore
    async def _get_repository(client: AsyncIOMotorClient = Depends(_get_client)):
        return repo(client.blog)

    return _get_repository
