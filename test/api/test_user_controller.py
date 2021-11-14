import json
from test.api.base_api_test_case import BaseApiTestCase
from test.api.mocks.mock_user_data import MockUserData
from test.api.mocks.mock_user_repository import MockSellerUserRepository
from test.api.mocks.mock_user_service import MockUserService
from test.utils import target_mock
from web.controller.user_controller import UserController
from web.repository.user_repository import UserRepository
from web.service.user_service import UserService


@target_mock.patch(target_module=UserController, target=UserService, new=MockUserService)
@target_mock.patch(target_module=UserService, target=UserRepository, new=MockSellerUserRepository)
class TestUserController(BaseApiTestCase):
    def test__create_user_with_valid_data(self):
        response = self.http_client.post(
            "/api/user/",
            headers=self._HEADERS,
            data=json.dumps(MockUserData.get_valid_create_user_request_data()),
        )
        self.assertEqual(response.status_code, 201)

    def test__create_user_with_missing_username(self):
        response = self.http_client.post(
            "/api/user/",
            headers=self._HEADERS,
            data=json.dumps(MockUserData.get_create_user_request_data_with_missing_username()),
        )
        self.assertEqual(response.status_code, 400)

    def test__create_user_with_empty_username(self):
        response = self.http_client.post(
            "/api/user/",
            headers=self._HEADERS,
            data=json.dumps(MockUserData.get_create_user_request_data_with_empty_username()),
        )
        self.assertEqual(response.status_code, 400)

    def test__create_user_with_invalid_role(self):
        response = self.http_client.post(
            "/api/user/",
            headers=self._HEADERS,
            data=json.dumps(MockUserData.get_create_user_request_data_with_invalid_role()),
        )
        self.assertEqual(response.status_code, 400)

    def test__get_user(self):
        response = self.http_client.get("/api/user/", headers=self._HEADERS)
        self.assertEqual(response.status_code, 200)
