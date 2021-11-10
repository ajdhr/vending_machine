from dataclasses import dataclass


@dataclass
class ProductDTO:
    name: str
    cost: int
    amount_available: int


@dataclass
class ProductResponseDTO(ProductDTO):
    id: int

