from typing import List

from flask_login import current_user

from db_factory import db
from web.dto.product_dto import ProductDTO, ProductResponseDTO
from web.model import Product
from web.utils.exceptions import ProductNotFoundException, ProductNotOwnedByUser


class ProductService:
    @classmethod
    def create(cls, data: ProductDTO):
        product = Product(seller_id=current_user.id)
        cls.__populate_product_model(product=product, data=data)

        db.session.add(product)
        db.session.commit()

    @classmethod
    def get(cls, product_id: int) -> ProductResponseDTO:
        product = cls.__get_by_id(product_id=product_id)
        return cls.__populate_product_response_dto(product=product)

    @classmethod
    def get_all(cls) -> List[ProductResponseDTO]:
        products: List[Product] = Product.query.all()
        return [cls.__populate_product_response_dto(product) for product in products]

    @classmethod
    def update(cls, product_id: int, data: ProductDTO):
        product = cls.__get_by_id(product_id=product_id)
        cls.__validate_ownership(product=product)

        cls.__populate_product_model(product=product, data=data)

        db.session.commit()

    @classmethod
    def delete(cls, product_id: int):
        product: Product = cls.__get_by_id(product_id=product_id)
        cls.__validate_ownership(product=product)

        Product.query.filter(Product.id == product_id).delete()

        db.session.commit()

    @classmethod
    def __validate_ownership(cls, product: Product):
        if not product.seller_id == current_user.id:
            raise ProductNotOwnedByUser(product_id=product.id)

    @classmethod
    def __populate_product_model(cls, product: Product, data: ProductDTO):
        product.name = data.name
        product.cost = data.cost
        product.amount_available = data.amount_available

    @classmethod
    def __get_by_id(cls, product_id: int) -> Product:
        product = Product.query.filter(Product.id == product_id).first()

        if not product:
            raise ProductNotFoundException(product_id=product_id)

        return product

    @classmethod
    def __populate_product_response_dto(cls, product: Product) -> ProductResponseDTO:
        return ProductResponseDTO(
            id=product.id,
            name=product.name,
            cost=product.cost,
            amount_available=product.amount_available,
        )
