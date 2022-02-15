from marshmallow import fields, validate, EXCLUDE
from marshmallow.validate import OneOf

from api.schemas import BaseSchema

CLOTHING_TYPE = ["JEANS", "TSHIRTS"]


class ClothingSchema(BaseSchema):
    clothing_type = fields.String(validate=OneOf(CLOTHING_TYPE), required=True, blank=False)

    class Meta:
        unknown = EXCLUDE
