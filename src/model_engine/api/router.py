"""All Routes."""
from fastapi import APIRouter
from server_config import health_router
from api import interpolation_router, generate_images_router

api_router = APIRouter()

# Health endpoint.
api_router.include_router(health_router, prefix="/health")
api_router.include_router(interpolation_router, prefix="/api/v1")
api_router.include_router(generate_images_router, prefix="/api/v1")
