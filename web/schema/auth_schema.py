import dacite
from marshmallow import Schema, fields, post_load
from marshmallow.validate import Length

from web.dto.auth_dto import AuthDTO


class AuthSchema(Schema):
    username = fields.String(required=True, allow_none=False, validate=Length(min=1, error="Username can not be empty"))
    password = fields.String(required=True, allow_none=False, validate=Length(min=1, error="Password can not be empty"))

    @post_load
    def load_to_dto(self, data, *args, **kwargs):
        return dacite.from_dict(data_class=AuthDTO, data=data)
