from typing import List

from web.dto.product_dto import ProductDTO, ProductResponseDTO


class MockProductService:
    @classmethod
    def create(cls, data: ProductDTO) -> ProductResponseDTO:
        return cls.__get_product_mock_response()

    @classmethod
    def get(cls, product_id: int) -> ProductResponseDTO:
        return cls.__get_product_mock_response()

    @classmethod
    def get_all(cls) -> List[ProductResponseDTO]:
        return [cls.__get_product_mock_response()]

    @classmethod
    def update(cls, product_id: int, data: ProductDTO) -> ProductResponseDTO:
        return cls.__get_product_mock_response()

    @classmethod
    def delete(cls, product_id: int):
        return

    @classmethod
    def __get_product_mock_response(cls) -> ProductResponseDTO:
        return ProductResponseDTO(id=1, name="TestProduct", cost=10, amount_available=10)
