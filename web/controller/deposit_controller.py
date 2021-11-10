from flask import request, Response
from flask_login import login_required
from flask_restplus import Resource, Namespace

from role import buyer_permission
from web.dto.deposit_dto import DepositDTO
from web.schema.deposit_schema import DepositSchema
from web.service.transaction_service import TransactionService

api = Namespace("deposit", description="Deposit namespace")


@api.route("/")
class DepositController(Resource):
    @login_required
    @buyer_permission.require(http_exception=403)
    def post(self):
        deposit_data: DepositDTO = DepositSchema().load(request.json)
        TransactionService.deposit(data=deposit_data)

        return Response(status=201)
