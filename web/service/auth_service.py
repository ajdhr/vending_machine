from flask import current_app
from flask_login import login_user, logout_user
from flask_principal import identity_changed, Identity
from werkzeug.security import check_password_hash

from web.dto.auth_dto import AuthDTO
from web.model import User
from web.utils.exceptions import InvalidUserCredentials


class AuthService:
    @classmethod
    def login(cls, data: AuthDTO):
        user: User = User.query.filter(User.username == data.username).first()

        if not user or not check_password_hash(pwhash=user.password, password=data.password):
            raise InvalidUserCredentials()

        login_user(user, remember=True)
        identity_changed.send(current_app._get_current_object(), identity=Identity(user.id))

    @classmethod
    def logout(cls):
        logout_user()
