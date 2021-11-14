from typing import Optional

from flask_login import current_user


class CurrentUserRepository:
    @staticmethod
    def get_current_user_id() -> Optional[int]:
        if current_user.is_anonymous:
            return None

        return current_user.id
