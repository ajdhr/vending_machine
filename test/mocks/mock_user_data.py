from web.model import User


class MockUserData:
    @staticmethod
    def get_valid_create_user_request_data():
        return {"username": "testUser", "password": "test123", "role": "buyer"}

    @staticmethod
    def get_valid_update_user_request_data():
        return {"username": "testUserUpdated", "password": "test123Updated", "role": "buyer"}

    @staticmethod
    def get_create_user_request_data_with_missing_username():
        return {"password": "pass", "role": "buyer"}

    @staticmethod
    def get_create_user_request_data_with_empty_username():
        return {"username": "", "password": "pass", "role": "buyer"}

    @staticmethod
    def get_create_user_request_data_with_invalid_role():
        return {"username": "test", "password": "pass", "role": "some_role"}

    @staticmethod
    def get_mock_seller_user() -> User:
        return User(id=1, username="testSeller", role="seller", deposit=0)

    @staticmethod
    def get_mock_buyer_user() -> User:
        return User(id=2, username="testBuyer", role="buyer", deposit=10)
