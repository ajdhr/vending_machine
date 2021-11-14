from test.mocks.mock_user_data import MockUserData


class MockCurrentUserSellerRepository:
    @staticmethod
    def get_current_user_id() -> int:
        return MockUserData.get_mock_seller_user().id


class MockCurrentUserBuyerRepository:
    @staticmethod
    def get_current_user_id() -> int:
        return MockUserData.get_mock_buyer_user().id
