from web.dto.deposit_dto import DepositDTO
from web.dto.transaction_dto import TransactionDTO, TransactionResultDTO


class MockTransactionService:
    @classmethod
    def deposit(cls, data: DepositDTO):
        return

    @classmethod
    def reset(cls):
        return

    @classmethod
    def buy_product(cls, data: TransactionDTO) -> TransactionResultDTO:
        return TransactionResultDTO(product_id=1, amount=1, change=[10])
