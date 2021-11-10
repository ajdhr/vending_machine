import dacite
from marshmallow import Schema, fields, post_load

from web.dto.product_dto import ProductDTO


class BaseProductSchema(Schema):
    name = fields.String(required=True, allow_none=False)
    cost = fields.Integer(required=True, allow_none=False)
    amount_available = fields.Integer(required=True, allow_none=False)


class ProductSchema(BaseProductSchema):
    @post_load
    def load_to_dto(self, data, *args, **kwargs):
        return dacite.from_dict(data_class=ProductDTO, data=data)


class ProductResponseSchema(BaseProductSchema):
    id = fields.Integer(required=True, allow_none=False)
