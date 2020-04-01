from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware

from blog_service.core.config import PROJECT_NAME, DEBUG, VERSION, ALLOWED_HOSTS, API_PREFIX
from blog_service.core.events import create_start_app_handler, create_stop_app_handler
from blog_service.routers.router import get_router

default_router = APIRouter()

@default_router.get('/')
async def index():
    return {"status": "ok"}

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

    application.include_router(get_router(), prefix=API_PREFIX)
    application.include_router(default_router)
    
    return application


app = get_application()

