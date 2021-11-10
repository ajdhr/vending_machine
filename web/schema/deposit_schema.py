import dacite
from marshmallow import Schema, fields, post_load
from marshmallow.validate import OneOf

from web.dto.deposit_dto import DepositDTO
from web.utils.constants import COIN_VALUES


class DepositSchema(Schema):
    amount = fields.Integer(required=True, allow_none=False, validate=OneOf(COIN_VALUES))

    @post_load
    def load_to_dto(self, data, *args, **kwargs):
        return dacite.from_dict(data_class=DepositDTO, data=data)
