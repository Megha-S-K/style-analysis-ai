from fastapi import FastAPI
from app.core.config import settings
from app.api.health import router as health_router

app = FastAPI(
    title=settings.APP_NAME,
    docs_url="/docs" if settings.ENV == "development" else None,
    redoc_url=None
)

app.include_router(
    health_router,
    prefix=settings.API_V1_PREFIX,
    tags=["Health"]
)
