import json
from test.base_api_test_case import BaseApiTestCase
from test.mocks.mock_deposit_data import MockDepositData
from test.mocks.mock_transaction_service import MockTransactionService
from test.mocks.mock_user_repository import MockBuyerUserRepository, MockSellerUserRepository
from test.utils import target_mock
from web.controller.deposit_controller import DepositController
from web.repository.user_repository import UserRepository
from web.service.transaction_service import TransactionService
from web.service.user_service import UserService


@target_mock.patch(target_module=DepositController, target=TransactionService, new=MockTransactionService)
class TestDepositController(BaseApiTestCase):
    @target_mock.patch(target_module=UserService, target=UserRepository, new=MockBuyerUserRepository)
    def test__deposit_valid_data_with_buyer_user(self):
        response = self.http_client.post(
            "/api/deposit/",
            headers=self._HEADERS,
            data=json.dumps(MockDepositData.get_valid_deposit_data()),
        )
        self.assertEqual(response.status_code, 200)

    @target_mock.patch(target_module=UserService, target=UserRepository, new=MockSellerUserRepository)
    def test__deposit_valid_data_with_seller_user(self):
        response = self.http_client.post(
            "/api/deposit/",
            headers=self._HEADERS,
            data=json.dumps(MockDepositData.get_valid_deposit_data()),
        )
        self.assertEqual(response.status_code, 403)

    @target_mock.patch(target_module=UserService, target=UserRepository, new=MockBuyerUserRepository)
    def test__deposit_invalid_data_with_buyer_user(self):
        response = self.http_client.post(
            "/api/deposit/",
            headers=self._HEADERS,
            data=json.dumps(MockDepositData.get_invalid_deposit_data()),
        )
        self.assertEqual(response.status_code, 400)
