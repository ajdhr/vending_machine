from typing import List

from web.model import Product
from web.utils.exceptions import ProductNotFoundException


class ProductRepository:
    @staticmethod
    def get_by_id(product_id: int) -> Product:
        product = Product.query.filter(Product.id == product_id).first()

        if not product:
            raise ProductNotFoundException(product_id=product_id)

        return product

    @staticmethod
    def get_all() -> List[Product]:
        return Product.query.all()
