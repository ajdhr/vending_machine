import json
from test.api.base_api_test_case import BaseApiTestCase
from test.api.mocks.mock_user_data import MockUserData
from test.api.mocks.mock_user_service import MockUserService
from utils import target_mock
from web.controller.user_controller import UserController
from web.service.user_service import UserService


@target_mock.patch(target_module=UserController, target=UserService, new=MockUserService)
class TestUserController(BaseApiTestCase):
    def test__create_user__valid_data(self):
        response = self.http_client.post(
            "/api/user/",
            headers=self._HEADERS,
            data=json.dumps(MockUserData.get_valid_create_user_request_data()),
        )
        self.assertEqual(response.status_code, 201)

    def test__create_user__missing_data(self):
        response = self.http_client.post(
            "/api/user/",
            headers=self._HEADERS,
            data=json.dumps(MockUserData.get_create_user_request_data_with_missing_field()),
        )
        self.assertEqual(response.status_code, 400)
