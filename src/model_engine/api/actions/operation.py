from fastapi import APIRouter, Request
from api.actions import PRODUCT_TYPE_TO_SCHEMA_MAP
import logging
from extensions import BadRequestException

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post(
    "/operations",
    tags=["Operations API"],
    summary="[API] - Operations",
    description="""
        Return {
            "status": "success",
            "result": {}
        }
        if successful
    """,
    response_description="""
        Success
    """
)
async def operations(request: Request):
    # try:
    request_data = await request.json()
    product_type = request_data.get("product_type", None)
    schema = PRODUCT_TYPE_TO_SCHEMA_MAP[product_type]()
    schema_data = schema.load(request_data)
    print(schema.load(request_data))
    result = {'schema_data': schema_data}
    return {"status": "success", "result": result}
    # except Exception as e:
    #     logger.error("Error in Operations API: {}".format(e))
    #     raise BadRequestException(e)
