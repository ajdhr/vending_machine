from test.mocks.mock_user_data import MockUserData
from web.model import Product


class MockProductData:
    @staticmethod
    def get_valid_product_request_data() -> dict:
        return {"name": "testProduct", "cost": 1, "amount_available": 3}

    @staticmethod
    def get_mock_product(seller_id: int, amount: int = 20, cost: int = 10) -> Product:
        return Product(id=1, name="MockProduct", cost=cost, amount_available=amount, seller_id=seller_id)

