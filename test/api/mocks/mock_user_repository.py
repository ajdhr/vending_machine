from test.api.mocks.mock_user_data import MockUserData
from web.model import User


class MockSellerUserRepository:
    @staticmethod
    def get_by_id(id: int) -> User:
        return MockUserData.get_mock_seller_user()

    @staticmethod
    def get_current_user() -> User:
        return MockUserData.get_mock_seller_user()


class MockBuyerUserRepository:
    @staticmethod
    def get_by_id(id: int) -> User:
        return MockUserData.get_mock_buyer_user()

    @staticmethod
    def get_current_user() -> User:
        return MockUserData.get_mock_buyer_user()
