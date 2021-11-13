import dacite
from marshmallow import Schema, fields, post_load

from web.dto.transaction_dto import TransactionDTO


class TransactionSchema(Schema):
    product_id = fields.Integer(required=True, allow_none=False)
    amount = fields.Integer(required=True, allow_none=False)

    @post_load
    def load_to_dto(self, data, *args, **kwargs):
        return dacite.from_dict(data_class=TransactionDTO, data=data)


class TransactionResponseSchema(Schema):
    product_id = fields.Integer(required=True, allow_none=False)
    amount = fields.Integer(required=True, allow_none=False)
    change = fields.List(fields.Integer(), required=True, allow_none=False, allow_empty=True)
