import json
from typing import List

from db_factory import db
from test.base_api_test_case import BaseApiTestCase
from test.integration.fixtures.product_fixtures import ProductFixtures
from test.integration.fixtures.user_fixtures import UserFixtures
from test.mocks.mock_buy_data import MockBuyData
from test.mocks.mock_current_user_repository import MockCurrentUserBuyerRepository
from test.utils import target_mock
from web.model import User, Product
from web.repository.current_user_repository import CurrentUserRepository
from web.repository.user_repository import UserRepository
from web.service.user_service import UserService


class TestBuyApi(BaseApiTestCase):
    @target_mock.patch(target_module=UserRepository, target=CurrentUserRepository, new=MockCurrentUserBuyerRepository)
    @target_mock.patch(target_module=UserService, target=CurrentUserRepository, new=MockCurrentUserBuyerRepository)
    def test__buy_valid_data(self):
        self.__test_variable_buy(
            deposit=20,
            available_amount=20,
            product_cost=10,
            requested_amount=1,
            expected_change=[10],
        )

    @target_mock.patch(target_module=UserRepository, target=CurrentUserRepository, new=MockCurrentUserBuyerRepository)
    @target_mock.patch(target_module=UserService, target=CurrentUserRepository, new=MockCurrentUserBuyerRepository)
    def test__buy_valid_data_greater_exact_change(self):
        self.__test_variable_buy(
            deposit=100,
            available_amount=20,
            product_cost=10,
            requested_amount=1,
            expected_change=[50, 20, 20],
        )

    @target_mock.patch(target_module=UserRepository, target=CurrentUserRepository, new=MockCurrentUserBuyerRepository)
    @target_mock.patch(target_module=UserService, target=CurrentUserRepository, new=MockCurrentUserBuyerRepository)
    def test__buy_valid_data_greater_inexact_change(self):
        self.__test_variable_buy(
            deposit=100,
            available_amount=20,
            product_cost=13,
            requested_amount=1,
            expected_change=[50, 20, 10, 5],
        )

    @target_mock.patch(target_module=UserRepository, target=CurrentUserRepository, new=MockCurrentUserBuyerRepository)
    @target_mock.patch(target_module=UserService, target=CurrentUserRepository, new=MockCurrentUserBuyerRepository)
    def test__buy_valid_data_multiple_products(self):
        self.__test_variable_buy(
            deposit=100,
            available_amount=20,
            product_cost=10,
            requested_amount=3,
            expected_change=[50, 20],
        )

    @target_mock.patch(target_module=UserRepository, target=CurrentUserRepository, new=MockCurrentUserBuyerRepository)
    @target_mock.patch(target_module=UserService, target=CurrentUserRepository, new=MockCurrentUserBuyerRepository)
    def test__buy_invalid_data_nonexistent_product(self):
        UserFixtures.add_mock_buyer_user(deposit=20)
        buy_data = MockBuyData.get_buy_request_data(product_id=222, amount=1)

        response = self.http_client.post("/api/buy/", headers=self._HEADERS, data=json.dumps(buy_data))

        self.assertEqual(response.status_code, 404)

    @target_mock.patch(target_module=UserRepository, target=CurrentUserRepository, new=MockCurrentUserBuyerRepository)
    @target_mock.patch(target_module=UserService, target=CurrentUserRepository, new=MockCurrentUserBuyerRepository)
    def test__buy_invalid_data_insufficient_funds(self):
        UserFixtures.add_mock_buyer_user(deposit=5)
        mock_product = ProductFixtures.add_mock_product(amount=10, cost=10)
        buy_data = MockBuyData.get_buy_request_data(product_id=mock_product.id, amount=3)

        response = self.http_client.post("/api/buy/", headers=self._HEADERS, data=json.dumps(buy_data))

        self.assertEqual(response.status_code, 400)

    @target_mock.patch(target_module=UserRepository, target=CurrentUserRepository, new=MockCurrentUserBuyerRepository)
    @target_mock.patch(target_module=UserService, target=CurrentUserRepository, new=MockCurrentUserBuyerRepository)
    def test__buy_invalid_data_insufficient_product_amount(self):
        UserFixtures.add_mock_buyer_user(deposit=500)
        mock_product = ProductFixtures.add_mock_product(amount=10, cost=10)
        buy_data = MockBuyData.get_buy_request_data(product_id=mock_product.id, amount=13)

        response = self.http_client.post("/api/buy/", headers=self._HEADERS, data=json.dumps(buy_data))

        self.assertEqual(response.status_code, 400)

    def __test_variable_buy(
        self,
        deposit: int,
        available_amount: int,
        product_cost: int,
        requested_amount: int,
        expected_change: List[int]
    ):
        mock_user = UserFixtures.add_mock_buyer_user(deposit=deposit)
        mock_product = ProductFixtures.add_mock_product(amount=available_amount, cost=product_cost)

        initial_product_amount = mock_product.amount_available

        buy_data = MockBuyData.get_buy_request_data(product_id=mock_product.id, amount=requested_amount)

        response = self.http_client.post("/api/buy/", headers=self._HEADERS, data=json.dumps(buy_data))

        user = db.session.query(User).filter(User.id == mock_user.id).first()
        product = db.session.query(Product).filter(Product.id == mock_product.id).first()

        deserialized_response = json.loads(response.data)

        self.assertEqual(user.deposit, 0)
        self.assertEqual(product.amount_available, initial_product_amount - buy_data.get("amount"))
        self.assertEqual(deserialized_response.get("product_id"), mock_product.id)
        self.assertEqual(deserialized_response.get("amount"), buy_data.get("amount"))
        self.assertEqual(deserialized_response.get("change"), expected_change)
