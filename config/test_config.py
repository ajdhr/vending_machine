from config.base_config import BaseConfig


class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "sqlite:///db_test.sqlite"
    DEBUG = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
