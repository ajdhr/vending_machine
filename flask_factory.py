from flask import Flask
from flask_login import LoginManager
from flask_principal import Principal, UserNeed, RoleNeed, identity_loaded

from db_factory import db
from web import blueprint
from web.service.user_service import UserService


def create_app(config):
    app = Flask(config.APP_NAME)
    app.config.from_object(config)

    db.init_app(app)
    setup_login_manager(app=app)
    app.register_blueprint(blueprint=blueprint)

    principals = Principal(app)
    identity_loaded.connect(on_identity_loaded)

    return app


def setup_login_manager(app):
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return UserService.get_by_id(id=user_id)


def on_identity_loaded(sender, identity):
    user = UserService.get()
    if not user:
        return

    identity.user = user

    if hasattr(user, "id"):
        identity.provides.add(UserNeed(user.id))

    if hasattr(user, "role"):
        identity.provides.add(RoleNeed(str(user.role.value)))
