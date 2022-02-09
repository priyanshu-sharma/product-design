from marshmallow import fields, validate, EXCLUDE
from marshmallow.validate import OneOf

from api.schemas import BaseSchema

ACCESSORIES_TYPE = ["HANDBAGS", "WATCHES", "JEWELLERY"]


class AccessoriesSchema(BaseSchema):
    accessories_type = fields.String(validate=OneOf(ACCESSORIES_TYPE), required=True, blank=False)

    class Meta:
        unknown = EXCLUDE
