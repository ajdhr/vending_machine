from db_factory import db
from test.mocks.mock_product_data import MockProductData
from web.model import Product


class ProductFixtures:
    @staticmethod
    def add_mock_product(seller_id: int, amount: int = 10, cost: int = 10) -> Product:
        product = MockProductData.get_mock_product(amount=amount, cost=cost, seller_id=seller_id)
        db.session.add(product)
        db.session.commit()

        return product
