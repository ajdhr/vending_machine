from typing import List

from db_factory import db
from web.dto.product_dto import ProductDTO, ProductResponseDTO
from web.model import Product
from web.repository.current_user_repository import CurrentUserRepository
from web.repository.product_repository import ProductRepository
from web.utils.exceptions import ProductNotOwnedByUser


class ProductService:
    @classmethod
    def create(cls, data: ProductDTO) -> ProductResponseDTO:
        product = Product(seller_id=CurrentUserRepository.get_current_user_id())
        cls.__populate_product_model(product=product, data=data)

        db.session.add(product)
        db.session.commit()

        return cls.__populate_product_response_dto(product=product)

    @classmethod
    def get(cls, product_id: int) -> ProductResponseDTO:
        product = ProductRepository.get_by_id(product_id=product_id)
        return cls.__populate_product_response_dto(product=product)

    @classmethod
    def get_all(cls) -> List[ProductResponseDTO]:
        products: List[Product] = ProductRepository.get_all()
        return [cls.__populate_product_response_dto(product=product) for product in products]

    @classmethod
    def update(cls, product_id: int, data: ProductDTO) -> ProductResponseDTO:
        product = ProductRepository.get_by_id(product_id=product_id)
        cls.__validate_ownership(product=product)

        cls.__populate_product_model(product=product, data=data)

        db.session.commit()

        return cls.__populate_product_response_dto(product=product)

    @classmethod
    def delete(cls, product_id: int):
        product: Product = ProductRepository.get_by_id(product_id=product_id)
        cls.__validate_ownership(product=product)

        Product.query.filter(Product.id == product_id).delete()

        db.session.commit()

    @classmethod
    def __validate_ownership(cls, product: Product):
        if not product.seller_id == CurrentUserRepository.get_current_user_id():
            raise ProductNotOwnedByUser(product_id=product.id)

    @classmethod
    def __populate_product_model(cls, product: Product, data: ProductDTO):
        product.name = data.name
        product.cost = data.cost
        product.amount_available = data.amount_available

    @classmethod
    def __populate_product_response_dto(cls, product: Product) -> ProductResponseDTO:
        return ProductResponseDTO(
            id=product.id,
            name=product.name,
            cost=product.cost,
            amount_available=product.amount_available,
        )
