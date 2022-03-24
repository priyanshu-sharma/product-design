from fastapi import APIRouter, Request
from api.actions import PRODUCT_TYPE_TO_SCHEMA_MAP
import logging
from extensions import BadRequestException

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post(
    "/interpolations",
    tags=["Interpolations API"],
    summary="[API] - Interpolations",
    description="""
        Return {
            "status": "success",
            "result": {}
        }
        if successful
    """,
    response_description="""
        Success
    """,
)
async def interpolations(request: Request):
    from layers import InterpolationLayer

    try:
        request_data = await request.json()
        product_type = request_data.get("product_type", None)
        # schema = PRODUCT_TYPE_TO_SCHEMA_MAP[product_type]()
        # schema_data = schema.load(request_data)
        images = request_data.get('images', [])
        interpolation_type = request_data.get("interpolation_type", None)
        interpolation_result = InterpolationLayer().transform(interpolation_type, images)
        return {"status": "success", "result": interpolation_result}
    except Exception as e:
        logger.error("Error in Interpolation API: {}".format(e))
        raise BadRequestException(e)
