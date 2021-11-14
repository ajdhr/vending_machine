from db_factory import db
from test.mocks.mock_user_data import MockUserData
from web.model import User


class UserFixtures:
    @staticmethod
    def add_mock_buyer_user(deposit: int = 0) -> User:
        user = MockUserData.get_mock_buyer_user(deposit=deposit)
        db.session.add(user)
        db.session.commit()

        return user

    @staticmethod
    def add_mock_seller_user() -> User:
        user = MockUserData.get_mock_seller_user()
        db.session.add(user)
        db.session.commit()

        return user
