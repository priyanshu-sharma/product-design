"""All Routes."""
from fastapi import APIRouter
from server_config import health_router

api_router = APIRouter()

# Health endpoint.
api_router.include_router(health_router, prefix="/health")

