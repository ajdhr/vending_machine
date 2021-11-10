from db_factory import db
from web.dto.deposit_dto import DepositDTO
from web.repository.user_repository import UserRepository


class TransactionService:
    @classmethod
    def deposit(cls, data: DepositDTO):
        user = UserRepository.get_current_user()
        user.deposit += data.amount

        db.session.commit()

    @classmethod
    def reset(cls):
        user = UserRepository.get_current_user()
        user.deposit = 0

        db.session.commit()
