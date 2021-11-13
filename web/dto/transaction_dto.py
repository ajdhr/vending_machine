from dataclasses import dataclass
from typing import List


@dataclass
class TransactionDTO:
    product_id: int
    amount: int


@dataclass
class TransactionResultDTO:
    product_id: int
    amount: int
    change: List[int]
