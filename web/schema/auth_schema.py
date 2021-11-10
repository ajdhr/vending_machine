import dacite
from marshmallow import Schema, fields, post_load

from web.dto.auth_dto import AuthDTO


class AuthSchema(Schema):
    username = fields.String(required=True, allow_none=False)
    password = fields.String(required=True, allow_none=False)

    @post_load
    def load_to_dto(self, data, *args, **kwargs):
        return dacite.from_dict(data_class=AuthDTO, data=data)
