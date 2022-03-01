import logging
from fastapi import APIRouter
from starlette.responses import PlainTextResponse
from starlette.responses import Response

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get(
    "/liveness",
    summary="[Health] - Liveness",
    description="""
        Return OK if the endpoint is reachable
    """,
    response_description="""
        OK - All is well
    """,
    response_class=PlainTextResponse,
)
async def liveness():
    return "OK"


@router.get(
    "/readiness",
    summary="[Health] - Readiness",
    description="""
        Return OK if the endpoint is reachable and the database can be reached
    """,
    response_description="""
        I'M READY - 200
        I'M SQUIDWARD - 500
    """,
    response_class=PlainTextResponse,
)
async def readiness():
    from storage_backend import registry as storage_registry
    try:
        storage_registry.redis.client.ping()
    except Exception as e:
        return Response("Internal server error", status_code=500)
    return "OK"
