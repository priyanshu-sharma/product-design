"""All Routes."""
from fastapi import APIRouter
from model_engine.api import health 

api_router = APIRouter()

# Health endpoint.
api_router.include_router(health.router, prefix="/health")

