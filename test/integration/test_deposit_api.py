import json

from db_factory import db
from test.base_api_test_case import BaseApiTestCase
from test.integration.fixtures.user_fixtures import UserFixtures
from test.mocks.mock_current_user_repository import MockCurrentUserBuyerRepository
from test.mocks.mock_deposit_data import MockDepositData
from test.utils import target_mock
from web.model import User
from web.repository.current_user_repository import CurrentUserRepository
from web.repository.user_repository import UserRepository
from web.service.user_service import UserService


class TestDepositApi(BaseApiTestCase):
    @target_mock.patch(target_module=UserRepository, target=CurrentUserRepository, new=MockCurrentUserBuyerRepository)
    @target_mock.patch(target_module=UserService, target=CurrentUserRepository, new=MockCurrentUserBuyerRepository)
    def test__deposit_valid_amount(self):
        mock_user = UserFixtures.add_mock_buyer_user()
        initial_deposit = mock_user.deposit
        deposit_data = MockDepositData.get_valid_deposit_data()

        self.http_client.post("/api/deposit/", headers=self._HEADERS, data=json.dumps(deposit_data))

        user = db.session.query(User).filter(User.id == mock_user.id).first()

        self.assertEqual(user.deposit, initial_deposit + deposit_data.get("amount"))
