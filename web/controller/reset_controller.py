from flask import Response
from flask_login import login_required
from flask_restplus import Resource, Namespace

from role import buyer_permission
from web.service.transaction_service import TransactionService

api = Namespace("reset", description="Reset namespace")


@api.route("/")
class ResetController(Resource):
    @login_required
    @buyer_permission.require(http_exception=403)
    @api.response(200, "Deposit successfully reset")
    @api.response(401, "Unauthorized access")
    @api.response(403, "Forbidden access")
    def post(self):
        TransactionService.reset()

        return Response(status=200)
