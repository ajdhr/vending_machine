from flask_testing import TestCase

from config.test_config import TestConfig
from db_factory import db
from flask_factory import create_app


class BaseApiTestCase(TestCase):
    def create_app(self):
        app = create_app(config=TestConfig)
        app.app_context().push()

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


