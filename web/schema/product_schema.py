import dacite
from marshmallow import Schema, fields, post_load
from marshmallow.validate import Length, Range

from web.dto.product_dto import ProductDTO


class BaseProductSchema(Schema):
    name = fields.String(required=True, allow_none=False, validate=Length(min=1, error="Product name can not be empty"))
    cost = fields.Integer(required=True, allow_none=False, validate=Range(min=1))
    amount_available = fields.Integer(required=True, allow_none=False, validate=Range(min=1))


class ProductSchema(BaseProductSchema):
    @post_load
    def load_to_dto(self, data, *args, **kwargs):
        return dacite.from_dict(data_class=ProductDTO, data=data)


class ProductResponseSchema(BaseProductSchema):
    id = fields.Integer(required=True, allow_none=False)
