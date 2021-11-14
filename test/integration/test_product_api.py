import json

from db_factory import db
from test.base_api_test_case import BaseApiTestCase
from test.integration.fixtures.product_fixtures import ProductFixtures
from test.integration.fixtures.user_fixtures import UserFixtures
from test.mocks.mock_current_user_repository import MockCurrentUserSellerRepository
from test.mocks.mock_product_data import MockProductData
from test.mocks.mock_user_data import MockUserData
from test.utils import target_mock
from web.model import Product
from web.repository.current_user_repository import CurrentUserRepository
from web.repository.user_repository import UserRepository
from web.service.product_service import ProductService
from web.service.user_service import UserService


class TestProductApi(BaseApiTestCase):
    @target_mock.patch(target_module=UserRepository, target=CurrentUserRepository, new=MockCurrentUserSellerRepository)
    @target_mock.patch(target_module=UserService, target=CurrentUserRepository, new=MockCurrentUserSellerRepository)
    @target_mock.patch(target_module=ProductService, target=CurrentUserRepository, new=MockCurrentUserSellerRepository)
    def test__create_product(self):
        UserFixtures.add_mock_seller_user()
        product_data = MockProductData.get_valid_product_request_data()
        self.http_client.post("/api/product/", headers=self._HEADERS, data=json.dumps(product_data))

        products = db.session.query(Product).all()

        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].name, product_data.get("name"))
        self.assertEqual(products[0].cost, product_data.get("cost"))
        self.assertEqual(products[0].amount_available, product_data.get("amount_available"))
        self.assertEqual(products[0].seller_id, MockUserData.get_mock_seller_user().id)

    @target_mock.patch(target_module=UserRepository, target=CurrentUserRepository, new=MockCurrentUserSellerRepository)
    @target_mock.patch(target_module=UserService, target=CurrentUserRepository, new=MockCurrentUserSellerRepository)
    @target_mock.patch(target_module=ProductService, target=CurrentUserRepository, new=MockCurrentUserSellerRepository)
    def test__get_products(self):
        UserFixtures.add_mock_seller_user()
        mock_product = ProductFixtures.add_mock_product()

        response = self.http_client.get("/api/product/", headers=self._HEADERS)
        deserialized_response = json.loads(response.data)

        self.assertEqual(len(deserialized_response), 1)
        self.assertEqual(mock_product.name, deserialized_response[0].get("name"))
        self.assertEqual(mock_product.cost, deserialized_response[0].get("cost"))
        self.assertEqual(mock_product.amount_available, deserialized_response[0].get("amount_available"))

    @target_mock.patch(target_module=UserRepository, target=CurrentUserRepository, new=MockCurrentUserSellerRepository)
    @target_mock.patch(target_module=UserService, target=CurrentUserRepository, new=MockCurrentUserSellerRepository)
    @target_mock.patch(target_module=ProductService, target=CurrentUserRepository, new=MockCurrentUserSellerRepository)
    def test__get_product(self):
        UserFixtures.add_mock_seller_user()
        mock_product = ProductFixtures.add_mock_product()

        response = self.http_client.get(f"/api/product/{mock_product.id}/", headers=self._HEADERS)
        deserialized_response = json.loads(response.data)

        self.assertEqual(mock_product.name, deserialized_response.get("name"))
        self.assertEqual(mock_product.cost, deserialized_response.get("cost"))
        self.assertEqual(mock_product.amount_available, deserialized_response.get("amount_available"))

    @target_mock.patch(target_module=UserRepository, target=CurrentUserRepository, new=MockCurrentUserSellerRepository)
    @target_mock.patch(target_module=UserService, target=CurrentUserRepository, new=MockCurrentUserSellerRepository)
    @target_mock.patch(target_module=ProductService, target=CurrentUserRepository, new=MockCurrentUserSellerRepository)
    def test__get_non_existent_product(self):
        UserFixtures.add_mock_seller_user()
        ProductFixtures.add_mock_product()

        response = self.http_client.get(f"/api/product/{123}/", headers=self._HEADERS)
        self.assertEqual(response.status_code, 404)

    @target_mock.patch(target_module=UserRepository, target=CurrentUserRepository, new=MockCurrentUserSellerRepository)
    @target_mock.patch(target_module=UserService, target=CurrentUserRepository, new=MockCurrentUserSellerRepository)
    @target_mock.patch(target_module=ProductService, target=CurrentUserRepository, new=MockCurrentUserSellerRepository)
    def test__update_product(self):
        UserFixtures.add_mock_seller_user()
        mock_product = ProductFixtures.add_mock_product()
        product_data = MockProductData.get_valid_product_request_data()

        self.http_client.put(f"/api/product/{mock_product.id}/", headers=self._HEADERS, data=json.dumps(product_data))

        product = db.session.query(Product).filter(Product.id == mock_product.id).first()

        self.assertEqual(product.name, product_data.get("name"))
        self.assertEqual(product.cost, product_data.get("cost"))
        self.assertEqual(product.amount_available, product_data.get("amount_available"))
        self.assertEqual(product.seller_id, MockUserData.get_mock_seller_user().id)

    @target_mock.patch(target_module=UserRepository, target=CurrentUserRepository, new=MockCurrentUserSellerRepository)
    @target_mock.patch(target_module=UserService, target=CurrentUserRepository, new=MockCurrentUserSellerRepository)
    @target_mock.patch(target_module=ProductService, target=CurrentUserRepository, new=MockCurrentUserSellerRepository)
    def test__update_non_existent_product(self):
        UserFixtures.add_mock_seller_user()
        ProductFixtures.add_mock_product()
        product_data = MockProductData.get_valid_product_request_data()

        response = self.http_client.put(f"/api/product/{222}/", headers=self._HEADERS, data=json.dumps(product_data))
        self.assertEqual(response.status_code, 404)

    @target_mock.patch(target_module=UserRepository, target=CurrentUserRepository, new=MockCurrentUserSellerRepository)
    @target_mock.patch(target_module=UserService, target=CurrentUserRepository, new=MockCurrentUserSellerRepository)
    @target_mock.patch(target_module=ProductService, target=CurrentUserRepository, new=MockCurrentUserSellerRepository)
    def test__delete_product(self):
        UserFixtures.add_mock_seller_user()
        mock_product = ProductFixtures.add_mock_product()

        self.http_client.delete(f"/api/product/{mock_product.id}/", headers=self._HEADERS)

        products = db.session.query(Product).all()
        self.assertEqual(len(products), 0)

    @target_mock.patch(target_module=UserRepository, target=CurrentUserRepository, new=MockCurrentUserSellerRepository)
    @target_mock.patch(target_module=UserService, target=CurrentUserRepository, new=MockCurrentUserSellerRepository)
    @target_mock.patch(target_module=ProductService, target=CurrentUserRepository, new=MockCurrentUserSellerRepository)
    def test__delete_non_existent_product(self):
        UserFixtures.add_mock_seller_user()
        ProductFixtures.add_mock_product()

        response = self.http_client.delete(f"/api/product/{222}/", headers=self._HEADERS)

        self.assertEqual(response.status_code, 404)
