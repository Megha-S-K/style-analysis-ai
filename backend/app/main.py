from app.api.upload import router as upload_router
from fastapi import FastAPI
from app.core.config import settings
from app.api.health import router as health_router
from app.api.preprocess import router as preprocess_router
from app.api.pose import router as pose_router
from app.api.measurements import router as measurements_router
from app.api.body_type import router as body_type_router
from app.api.skin_tone import router as skin_tone_router
from app.api.style import router as style_router
from app.api.explain import router as explain_router

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

app.include_router(
    measurements_router,
    prefix=settings.API_V1_PREFIX,
    tags=["Measurements"]
)

app.include_router(
    body_type_router,
    prefix=settings.API_V1_PREFIX,
    tags=["Body Type"]
)

app.include_router(
    skin_tone_router,
    prefix=settings.API_V1_PREFIX,
    tags=["Skin Tone"]
)

app.include_router(
    style_router,
    prefix=settings.API_V1_PREFIX,
    tags=["Style"]
)

app.include_router(
    explain_router,
    prefix=settings.API_V1_PREFIX,
    tags=["Explain"]
)
