from flask import request
from flask_login import login_required
from flask_restplus import Resource, Namespace

from role import buyer_permission
from web.dto.transaction_dto import TransactionDTO, TransactionResultDTO
from web.schema.transaction_schema import TransactionSchema, TransactionResponseSchema
from web.service.transaction_service import TransactionService

api = Namespace("buy", description="Buy namespace")


@api.route("/")
class DepositController(Resource):
    @login_required
    @buyer_permission.require(http_exception=403)
    def post(self):
        transaction_data: TransactionDTO = TransactionSchema().load(request.json)
        transaction_response: TransactionResultDTO = TransactionService.buy_product(data=transaction_data)

        response = TransactionResponseSchema().dump(transaction_response)

        return response, 200
