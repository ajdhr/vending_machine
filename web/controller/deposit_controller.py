from flask import request, Response
from flask_login import login_required
from flask_restplus import Resource, Namespace

from role import buyer_permission
from web.dto.deposit_dto import DepositDTO
from web.schema.deposit_schema import DepositSchema
from web.service.transaction_service import TransactionService
from web.utils.validation_error_handler import validation_error_handler

api = Namespace("deposit", description="Deposit namespace")


@api.route("/")
class DepositController(Resource):
    @login_required
    @buyer_permission.require(http_exception=403)
    @validation_error_handler
    @api.response(200, "Deposit successfully applied")
    @api.response(400, "Invalid request data")
    @api.response(401, "Unauthorized access")
    @api.response(403, "Forbidden access")
    def post(self):
        deposit_data: DepositDTO = DepositSchema().load(request.json)
        TransactionService.deposit(data=deposit_data)

        return Response(status=200)
