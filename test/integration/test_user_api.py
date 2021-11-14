import json

from db_factory import db
from test.base_api_test_case import BaseApiTestCase
from test.integration.fixtures.user_fixtures import UserFixtures
from test.mocks.mock_current_user_repository import MockCurrentUserSellerRepository, MockCurrentUserBuyerRepository
from test.mocks.mock_user_data import MockUserData
from test.utils import target_mock
from web.model import User
from web.repository.current_user_repository import CurrentUserRepository
from web.repository.user_repository import UserRepository
from web.service.user_service import UserService


class TestUserApi(BaseApiTestCase):
    @target_mock.patch(target_module=UserRepository, target=CurrentUserRepository, new=MockCurrentUserBuyerRepository)
    def test__create_user(self):
        self.http_client.post(
            "/api/user/",
            headers=self._HEADERS,
            data=json.dumps(MockUserData.get_valid_create_user_request_data()),
        )

        users = db.session.query(User).all()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, MockUserData.get_valid_create_user_request_data().get("username"))

    @target_mock.patch(target_module=UserRepository, target=CurrentUserRepository, new=MockCurrentUserSellerRepository)
    def test__get_user(self):
        user = UserFixtures.add_mock_seller_user()

        response = self.http_client.get("/api/user/", headers=self._HEADERS)
        deserialized_response = json.loads(response.data)

        self.assertEqual(user.username, deserialized_response.get("username"))
        self.assertEqual(user.deposit, deserialized_response.get("deposit"))

    @target_mock.patch(target_module=UserRepository, target=CurrentUserRepository, new=MockCurrentUserSellerRepository)
    def test__update_user(self):
        update_data = MockUserData.get_valid_update_user_request_data()
        user = UserFixtures.add_mock_seller_user()

        self.http_client.put(
            "/api/user/",
            headers=self._HEADERS,
            data=json.dumps(update_data),
        )

        user = db.session.query(User).filter(User.id == user.id).first()

        self.assertEqual(user.username, update_data.get("username"))

    @target_mock.patch(target_module=UserService, target=CurrentUserRepository, new=MockCurrentUserSellerRepository)
    @target_mock.patch(target_module=UserRepository, target=CurrentUserRepository, new=MockCurrentUserSellerRepository)
    def test__delete_user(self):
        user = UserFixtures.add_mock_seller_user()
        self.http_client.delete("/api/user/", headers=self._HEADERS)

        users = db.session.query(User).all()

        self.assertEqual(len(users), 0)
