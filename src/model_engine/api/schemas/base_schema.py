from marshmallow import Schema, fields
from marshmallow.validate import OneOf

PRODUCT_TYPE = ["CLOTHING", "ACCESSORIES"]
OPERATION_TYPE = ["SUBTRACT"]

class BaseSchema(Schema):
    product_type = fields.String(
        validate=OneOf(PRODUCT_TYPE), required=True, blank=False
    )
    image_names = fields.List(fields.String(), required=True, blank=False)
    meta = fields.Dict(required=True, blank=True)
    operation_type = fields.String(
        validate=OneOf(OPERATION_TYPE), required=True, blank=False
    )