from typing import Optional

from flask_login import current_user

from web.model import User
from web.repository.current_user_repository import CurrentUserRepository


class UserRepository:
    @staticmethod
    def get_current_user() -> Optional[User]:
        current_user_id = CurrentUserRepository.get_current_user_id()
        if not current_user_id:
            return None

        return User.query.filter(User.id == current_user_id).first()

    @staticmethod
    def get_by_id(id: int) -> User:
        return User.query.filter(User.id == id).first()
