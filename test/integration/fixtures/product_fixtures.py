from db_factory import db
from test.mocks.mock_product_data import MockProductData
from web.model import Product


class ProductFixtures:
    @staticmethod
    def add_mock_product() -> Product:
        product = MockProductData.get_mock_product()
        db.session.add(product)
        db.session.commit()

        return product
