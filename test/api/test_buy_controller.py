import json
from test.api.base_api_test_case import BaseApiTestCase
from test.api.mocks.mock_buy_data import MockBuyData
from test.api.mocks.mock_deposit_data import MockDepositData
from test.api.mocks.mock_transaction_service import MockTransactionService
from test.api.mocks.mock_user_repository import MockSellerUserRepository, MockBuyerUserRepository
from test.utils import target_mock
from web.controller.buy_controller import BuyController
from web.repository.user_repository import UserRepository
from web.service.transaction_service import TransactionService
from web.service.user_service import UserService


@target_mock.patch(target_module=BuyController, target=TransactionService, new=MockTransactionService)
class TestResetController(BaseApiTestCase):
    @target_mock.patch(target_module=UserService, target=UserRepository, new=MockBuyerUserRepository)
    def test__buy_valid_data_with_buyer_user(self):
        response = self.http_client.post(
            "/api/buy/",
            headers=self._HEADERS,
            data=json.dumps(MockBuyData.get_valid_buy_request_data()),
        )
        self.assertEqual(response.status_code, 200)

    @target_mock.patch(target_module=UserService, target=UserRepository, new=MockSellerUserRepository)
    def test__buy_valid_data_with_seller_user(self):
        response = self.http_client.post(
            "/api/buy/",
            headers=self._HEADERS,
            data=json.dumps(MockBuyData.get_valid_buy_request_data()),
        )
        self.assertEqual(response.status_code, 403)

    @target_mock.patch(target_module=UserService, target=UserRepository, new=MockBuyerUserRepository)
    def test__buy_invalid_data(self):
        response = self.http_client.post(
            "/api/buy/",
            headers=self._HEADERS,
            data=json.dumps(MockBuyData.get_buy_request_data_with_invalid_amount()),
        )
        self.assertEqual(response.status_code, 400)
