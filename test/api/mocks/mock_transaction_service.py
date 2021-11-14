from web.dto.deposit_dto import DepositDTO


class MockTransactionService:
    @classmethod
    def deposit(cls, data: DepositDTO):
        return

    @classmethod
    def reset(cls):
        return
