from marshmallow import Schema, fields
from marshmallow.validate import OneOf

PRODUCT_TYPE = ["CLOTHING", "ACCESSORIES"]
INTERPOLATION_TYPE = ["LINEAR", "ADD_CONSTANT"]

class BaseSchema(Schema):
    product_type = fields.String(
        validate=OneOf(PRODUCT_TYPE), required=True, blank=False
    )
    image_names = fields.List(fields.String(), required=True, blank=False)
    meta = fields.Dict(required=True, blank=True)
    interpolation_type = fields.String(
        validate=OneOf(INTERPOLATION_TYPE), required=True, blank=False
    )