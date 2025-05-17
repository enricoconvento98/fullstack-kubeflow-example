from fastapi import APIRouter
from .endpoints import pipeline, metrics

router = APIRouter()
router.include_router(pipeline.router, tags=["Pipelines"])
router.include_router(metrics.router, tags=["Metrics"])