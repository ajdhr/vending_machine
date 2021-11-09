from flask import Flask
from db_factory import db


def create_app(config):
    app = Flask(config.APP_NAME)
    app.config.from_object(config)

    db.init_app(app)

    return app
