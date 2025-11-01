from fastapi import FastAPI

from app.interfaces.api.routes import router as api_router
from app.settings import get_settings


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.

    :return: Configured FastAPI application instance.
    """
    settings = get_settings()

    _app = FastAPI(
        debug=settings.DEBUG,
        title=settings.name,
        version=settings.version,
        root_path=settings.root_path,
        description="A system to create and play a RPG game",
    )

    return _app


app = create_app()
app.include_router(api_router)
