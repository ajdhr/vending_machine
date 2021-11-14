from test.mocks.mock_user_data import MockUserData
from web.model import Product


class MockProductData:
    @staticmethod
    def get_valid_product_request_data() -> dict:
        return {"name": "testProduct", "cost": 1, "amount_available": 3}

    @staticmethod
    def get_mock_product() -> Product:
        seller_id = MockUserData.get_mock_seller_user().id
        return Product(id=1, name="MockProduct", cost=10, amount_available=20, seller_id=seller_id)

