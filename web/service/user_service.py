from flask_login import current_user
from werkzeug.security import generate_password_hash

from db_factory import db
from role import Role
from web.dto.user_dto import UserDTO, GetUserDTO
from web.model.user import User


class UserService:
    @classmethod
    def create(cls, data: UserDTO):
        user = User()
        cls.__populate_user_model(user=user, data=data)

        db.session.add(user)
        db.session.commit()

    @classmethod
    def get(cls) -> GetUserDTO:
        user = cls.__get_by_id(user_id=current_user.id)

        return cls.__populate_user_dto(user=user)

    @classmethod
    def update(cls, data: UserDTO):
        user = cls.__get_by_id(user_id=current_user.id)
        cls.__populate_user_model(user=user, data=data)

        db.session.commit()

    @classmethod
    def delete(cls):
        User.query.filter(User.id == current_user.id).delete()

    @classmethod
    def __populate_user_dto(cls, user: User) -> GetUserDTO:
        return GetUserDTO(username=user.username, role=Role(user.role), deposit=user.deposit)

    @classmethod
    def __get_by_id(cls, user_id: int) -> User:
        return User.query.filter(User.id == current_user.id).first()

    @classmethod
    def __populate_user_model(cls, user: User, data: UserDTO):
        user.username = data.username
        user.password = generate_password_hash(data.password, method="sha256")
        user.role = data.role.value
