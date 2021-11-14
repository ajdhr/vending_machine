from db_factory import db
from test.base_api_test_case import BaseApiTestCase
from test.integration.fixtures.user_fixtures import UserFixtures
from test.mocks.mock_current_user_repository import MockCurrentUserBuyerRepository
from test.utils import target_mock
from web.model import User
from web.repository.current_user_repository import CurrentUserRepository
from web.repository.user_repository import UserRepository
from web.service.user_service import UserService


class TestResetApi(BaseApiTestCase):
    @target_mock.patch(target_module=UserRepository, target=CurrentUserRepository, new=MockCurrentUserBuyerRepository)
    @target_mock.patch(target_module=UserService, target=CurrentUserRepository, new=MockCurrentUserBuyerRepository)
    def test__reset_deposit(self):
        mock_user = UserFixtures.add_mock_buyer_user(deposit=10)

        self.http_client.post("/api/reset/", headers=self._HEADERS)

        user = db.session.query(User).filter(User.id == mock_user.id).first()

        self.assertEqual(user.deposit, 0)
