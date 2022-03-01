from fastapi import APIRouter, Request
from api.actions import PRODUCT_TYPE_TO_SCHEMA_MAP
import logging
from extensions import BadRequestException

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post(
    "/generate_images",
    tags=["Generate Images API"],
    summary="[API] - Generate Images",
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
async def generate_images(request: Request):
    from layers import InterpolationLayer

    try:
        request_data = await request.json()
        product_type = request_data.get("product_type", None)
        interpolation_layer = InterpolationLayer()
        result = interpolation_layer.refresh(product_type)
        return {"status": "success", "result": str(result)}
    except Exception as e:
        logger.error("Error in Operations API: {}".format(e))
        raise BadRequestException(e)
