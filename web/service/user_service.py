from flask_login import current_user
from sqlalchemy import exists
from werkzeug.security import generate_password_hash

from db_factory import db
from role import Role
from web.dto.user_dto import UserDTO, UserResponseDTO
from web.model.user import User
from web.repository.user_repository import UserRepository
from web.utils.exceptions import UserAlreadyExists


class UserService:
    @classmethod
    def create(cls, data: UserDTO):
        if cls.__exists(username=data.username):
            raise UserAlreadyExists(username=data.username)

        user = User()
        cls.__populate_user_model(user=user, data=data)

        db.session.add(user)
        db.session.commit()

    @classmethod
    def get(cls) -> UserResponseDTO:
        user = UserRepository.get_current_user()

        return cls.__populate_user_dto(user=user)

    @classmethod
    def update(cls, data: UserDTO):
        user = UserRepository.get_current_user()
        cls.__populate_user_model(user=user, data=data)

        db.session.commit()

    @classmethod
    def delete(cls):
        User.query.filter(User.id == current_user.id).delete()

        db.session.commit()

    @classmethod
    def __populate_user_dto(cls, user: User) -> UserResponseDTO:
        return UserResponseDTO(username=user.username, role=Role(user.role), deposit=user.deposit)

    @classmethod
    def __populate_user_model(cls, user: User, data: UserDTO):
        user.username = data.username
        user.password = generate_password_hash(data.password, method="sha256")
        user.role = data.role.value

    @classmethod
    def __exists(cls, username: str) -> bool:
        return db.session.query(exists().where(User.username == username)).scalar()
