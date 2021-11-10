from flask import Flask
from flask_login import LoginManager

from db_factory import db
from web import blueprint


def create_app(config):
    app = Flask(config.APP_NAME)
    app.config.from_object(config)

    db.init_app(app)
    setup_login_manager(app=app)
    app.register_blueprint(blueprint=blueprint)

    return app


def setup_login_manager(app):
    login_manager = LoginManager()
    login_manager.init_app(app)

    from web.model.user import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
