from app.api.upload import router as upload_router
from fastapi import FastAPI
from app.core.config import settings
from app.api.health import router as health_router
from app.api.preprocess import router as preprocess_router
from app.api.pose import router as pose_router

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

app.include_router(
    upload_router,
    prefix=settings.API_V1_PREFIX,
    tags=["Upload"]
)

app.include_router(
    preprocess_router,
    prefix=settings.API_V1_PREFIX,
    tags=["Preprocess"]
)

app.include_router(
    pose_router,
    prefix=settings.API_V1_PREFIX,
    tags=["Pose"]
)

