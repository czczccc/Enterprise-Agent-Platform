from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.core.config import Settings, get_settings


def create_app(settings: Settings | None = None) -> FastAPI:
    application_settings = settings or get_settings()
    application = FastAPI(
        title=application_settings.app_name,
        version=application_settings.app_version,
    )
    application.include_router(health_router)
    return application


app = create_app()
