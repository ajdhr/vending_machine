from typing import List

from db_factory import db
from web.dto.transaction_dto import TransactionDTO, TransactionResultDTO
from web.dto.deposit_dto import DepositDTO
from web.model import Product, User
from web.repository.product_repository import ProductRepository
from web.repository.user_repository import UserRepository
from web.utils.constants import COIN_VALUES
from web.utils.exceptions import InsufficientFunds, ProductQuantityUnavailable


class TransactionService:
    @classmethod
    def deposit(cls, data: DepositDTO):
        user: User = UserRepository.get_current_user()
        user.deposit += data.amount

        db.session.commit()

    @classmethod
    def reset(cls):
        user: User = UserRepository.get_current_user()
        user.deposit = 0

        db.session.commit()

    @classmethod
    def buy_product(cls, data: TransactionDTO) -> TransactionResultDTO:
        product: Product = ProductRepository.get_by_id(product_id=data.product_id)
        user: User = UserRepository.get_current_user()

        cls.__validate_product_quantity(product=product, amount_requested=data.amount)
        cls.__validate_funds(amount=data.amount, cost=product.cost, deposit=user.deposit)

        change_coins = cls.__determine_change(amount=data.amount, cost=product.cost, deposit=user.deposit)

        user.deposit = 0
        product.amount_available -= data.amount

        db.session.commit()

        return TransactionResultDTO(product_id=data.product_id, amount=data.amount, change=change_coins)

    @classmethod
    def __validate_product_quantity(cls, product: Product, amount_requested: int):
        if product.amount_available < amount_requested:
            raise ProductQuantityUnavailable()

    @classmethod
    def __validate_funds(cls, amount: int, cost: int, deposit: int):
        if amount * cost > deposit:
            raise InsufficientFunds()

    @classmethod
    def __determine_change(cls, amount: int, cost: int, deposit: int) -> List[int]:
        total_change = deposit - amount * cost

        change_coins = []
        current_coin_index = 0
        available_coins = sorted(COIN_VALUES, reverse=True)

        while total_change > available_coins[-1] and current_coin_index < len(available_coins):
            current_coin = available_coins[current_coin_index]

            if total_change >= current_coin:
                change_coins.append(current_coin)
                total_change -= current_coin
            else:
                current_coin_index += 1

        return change_coins
