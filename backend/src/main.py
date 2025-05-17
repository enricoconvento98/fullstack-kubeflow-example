from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import DevelopmentConfig as config
from .api.endpoints import pipeline, metrics

app = FastAPI(debug=config.DEBUG)

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pipeline.router)
app.include_router(metrics.router)

@app.get("/")
def read_root():
    return {"message": "Fullstack Kubeflow Backend"}