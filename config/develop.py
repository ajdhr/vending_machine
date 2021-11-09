from config.base_config import BaseConfig


class DevelopConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "sqlite://db.sqlite"
    DEBUG = True
