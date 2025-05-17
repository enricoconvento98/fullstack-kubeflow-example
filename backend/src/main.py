from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from .config import settings
from .database import engine, Base
from .api import router as api_router
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    logger.info("Starting up...")
    Base.metadata.create_all(bind=engine)
    yield
    # Shutdown code
    logger.info("Shutting down...")

app = FastAPI(
    title="Kubeflow Pipeline Dashboard API",
    description="Backend for Fullstack Kubeflow Example",
    version="1.0.0",
    lifespan=lifespan
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Kubeflow Pipeline Dashboard API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}