from enums import ProductType
from api.schemas import ClothingSchema, AccessoriesSchema

PRODUCT_TYPE_TO_SCHEMA_MAP = {
    ProductType.CLOTHING.value: ClothingSchema,
    ProductType.ACCESSORIES.value: AccessoriesSchema,
}
