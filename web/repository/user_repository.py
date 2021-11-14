from flask_login import current_user

from web.model import User


class UserRepository:
    @staticmethod
    def get_current_user() -> User:
        return User.query.filter(User.id == current_user.id).first()

    @staticmethod
    def get_by_id(id: int) -> User:
        return User.query.filter(User.id == id).first()
