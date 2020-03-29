from fastapi import FastAPI
from blog_service.core.config import PROJECT_NAME, DEBUG, VERSION, ALLOWED_HOSTS, API_PREFIX
from starlette.middleware.cors import CORSMiddleware
from blog_service.core.events import create_start_app_handler, create_stop_app_handler
from blog_service.routers.router import router
import logging
from loguru import logger
from blog_service.core.logging import InterceptHandler
import sys


def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_event_handler(
        "startup", create_start_app_handler(application))
    application.add_event_handler(
        "shutdown", create_stop_app_handler(application))

    application.include_router(router, prefix=API_PREFIX)
    return application


app = get_application()