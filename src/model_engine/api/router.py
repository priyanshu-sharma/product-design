"""All Routes."""
from fastapi import APIRouter
from api import health 

api_router = APIRouter()

# Health endpoint.
api_router.include_router(health.router, prefix="/health")

