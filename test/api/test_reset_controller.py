from test.api.base_api_test_case import BaseApiTestCase
from test.api.mocks.mock_transaction_service import MockTransactionService
from test.api.mocks.mock_user_repository import MockSellerUserRepository, MockBuyerUserRepository
from test.utils import target_mock
from web.controller.reset_controller import ResetController
from web.repository.user_repository import UserRepository
from web.service.transaction_service import TransactionService
from web.service.user_service import UserService


@target_mock.patch(target_module=ResetController, target=TransactionService, new=MockTransactionService)
class TestResetController(BaseApiTestCase):
    @target_mock.patch(target_module=UserService, target=UserRepository, new=MockBuyerUserRepository)
    def test__reset_with_buyer_user(self):
        response = self.http_client.post("/api/reset/", headers=self._HEADERS)
        self.assertEqual(response.status_code, 200)

    @target_mock.patch(target_module=UserService, target=UserRepository, new=MockSellerUserRepository)
    def test__reset_with_seller_user(self):
        response = self.http_client.post("/api/reset/", headers=self._HEADERS)
        self.assertEqual(response.status_code, 403)
