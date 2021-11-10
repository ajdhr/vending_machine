from werkzeug.security import generate_password_hash

from db_factory import db
from web.dto.user_dto import CreateUserDTO
from web.model.user import User


class UserService:
    @classmethod
    def create(cls, data: CreateUserDTO):
        user = User(
            username=data.username,
            password=generate_password_hash(data.password, method="sha256"),
            role=data.role.value,
            deposit=0,
        )

        db.session.add(user)
        db.session.commit()
