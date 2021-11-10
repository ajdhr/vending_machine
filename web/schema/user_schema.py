import dacite
from marshmallow import Schema, fields, post_load
from marshmallow_enum import EnumField

from role import Role
from web.dto.user_dto import UserDTO


class UserSchema(Schema):
    username = fields.String(required=True, allow_none=False)
    password = fields.String(required=True, allow_none=False)
    role = EnumField(Role, required=True, allow_none=False)

    @post_load
    def load_to_dto(self, data, *args, **kwargs):
        return dacite.from_dict(data_class=UserDTO, data=data)


class GetUserSchema(Schema):
    username = fields.String(required=True, allow_none=False)
    role = EnumField(Role, required=True, allow_none=False)
    deposit = fields.Integer(required=True, allow_none=False)
