import json
from test.api.base_api_test_case import BaseApiTestCase
from test.api.mocks.mock_product_data import MockProductData
from test.api.mocks.mock_product_service import MockProductService
from test.api.mocks.mock_user_repository import MockBuyerUserRepository, MockSellerUserRepository
from test.utils import target_mock
from web.controller.product_controller import ProductController
from web.repository.user_repository import UserRepository
from web.service.product_service import ProductService
from web.service.user_service import UserService


@target_mock.patch(target_module=ProductController, target=ProductService, new=MockProductService)
class TestProductController(BaseApiTestCase):
    @target_mock.patch(target_module=UserService, target=UserRepository, new=MockBuyerUserRepository)
    def test__create_product_with_buyer_user(self):
        response = self.http_client.post(
            "/api/product/",
            headers=self._HEADERS,
            data=json.dumps(MockProductData.get_valid_product_request_data()),
        )
        self.assertEqual(response.status_code, 403)

    @target_mock.patch(target_module=UserService, target=UserRepository, new=MockSellerUserRepository)
    def test__create_product_with_seller_user(self):
        response = self.http_client.post(
            "/api/product/",
            headers=self._HEADERS,
            data=json.dumps(MockProductData.get_valid_product_request_data()),
        )
        self.assertEqual(response.status_code, 201)

    @target_mock.patch(target_module=UserService, target=UserRepository, new=MockBuyerUserRepository)
    def test__update_product_with_buyer_user(self):
        response = self.http_client.put(
            "/api/product/1/",
            headers=self._HEADERS,
            data=json.dumps(MockProductData.get_valid_product_request_data()),
        )
        self.assertEqual(response.status_code, 403)

    @target_mock.patch(target_module=UserService, target=UserRepository, new=MockSellerUserRepository)
    def test__update_product_with_seller_user(self):
        response = self.http_client.put(
            "/api/product/1/",
            headers=self._HEADERS,
            data=json.dumps(MockProductData.get_valid_product_request_data()),
        )
        self.assertEqual(response.status_code, 200)

    @target_mock.patch(target_module=UserService, target=UserRepository, new=MockBuyerUserRepository)
    def test__delete_product_with_buyer_user(self):
        response = self.http_client.delete("/api/product/1/", headers=self._HEADERS)
        self.assertEqual(response.status_code, 403)

    @target_mock.patch(target_module=UserService, target=UserRepository, new=MockSellerUserRepository)
    def test__delete_product_with_seller_user(self):
        response = self.http_client.delete("/api/product/1/", headers=self._HEADERS)
        self.assertEqual(response.status_code, 204)

    @target_mock.patch(target_module=UserService, target=UserRepository, new=MockBuyerUserRepository)
    def test__get_product_with_buyer_user(self):
        response = self.http_client.get("/api/product/1/", headers=self._HEADERS)
        self.assertEqual(response.status_code, 200)

    @target_mock.patch(target_module=UserService, target=UserRepository, new=MockSellerUserRepository)
    def test__get_product_with_seller_user(self):
        response = self.http_client.get("/api/product/1/", headers=self._HEADERS)
        self.assertEqual(response.status_code, 200)

    @target_mock.patch(target_module=UserService, target=UserRepository, new=MockBuyerUserRepository)
    def test__get_products_with_buyer_user(self):
        response = self.http_client.get("/api/product/", headers=self._HEADERS)
        self.assertEqual(response.status_code, 200)

    @target_mock.patch(target_module=UserService, target=UserRepository, new=MockSellerUserRepository)
    def test__get_products_with_seller_user(self):
        response = self.http_client.get("/api/product/", headers=self._HEADERS)
        self.assertEqual(response.status_code, 200)
