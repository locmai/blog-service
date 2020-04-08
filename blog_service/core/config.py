import logging
import sys
from typing import List

import pkg_resources
from loguru import logger
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

from blog_service.core.logging import InterceptHandler

config = Config(".env")

# Project information
PROJECT_NAME = "Blog Service"

DEBUG: bool = config("DEBUG", cast=bool, default=False)

VERSION = config("VERSION", default="0.0.0")

# API configuration
API_PREFIX = "/api"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  # 1 day

# JWT authentication
JWT_TOKEN_TYPE: str = "Bearer"
SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret)
ACCESS_TOKEN_EXPIRE_MINUTES: config("ACCESS_TOKEN_EXPIRE_MINUTES", cast=int, default=30)
ALGORITHM = "HS256"

# Database connection

DATABASE_URL: str = config("DATABASE_URL")
MAX_CONNECTIONS: int = config("MAX_CONNECTIONS", cast=int, default=10)
MIN_CONNECTIONS: int = config("MIN_CONNECTIONS", cast=int, default=0)
# CORS
ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS", cast=CommaSeparatedStrings, default=""
)


# Logging configurations

LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
logging.basicConfig(
    handlers=[InterceptHandler(level=LOGGING_LEVEL)], level=LOGGING_LEVEL
)
logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])
