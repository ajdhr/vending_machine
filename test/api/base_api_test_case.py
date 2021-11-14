from flask import current_app
from flask_login import login_user
from flask_principal import identity_changed, Identity
from flask_testing import TestCase

from config.test_config import TestConfig
from db_factory import db
from flask_factory import create_app
from role import Role
from web.model import User


class BaseApiTestCase(TestCase):
    def create_app(self):
        app = create_app(config=TestConfig)
        app.app_context().push()

        @app.before_request
        def get_identity():
            identity_changed.send(current_app._get_current_object(), identity=Identity(Role.buyer.value))

        return app

    def setUp(self, *args, **kwargs):
        self.http_client = self.app.test_client()
        self._HEADERS = {
            "Content-type": "application/json",
            "Accept": "application/json",
        }

        super().setUp(*args, **kwargs)

    def tearDown(self, *args, **kwargs):
        super().tearDown(*args, **kwargs)
        db.session.remove()
        db.drop_all()

    @staticmethod
    def _login_mock_user(user: User):
        login_user(user, remember=True)
        identity_changed.send(current_app._get_current_object(), identity=Identity(user.id))
