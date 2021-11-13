from flask import request, Response
from flask_restplus import Namespace, Resource

from web.dto.auth_dto import AuthDTO
from web.schema.auth_schema import AuthSchema
from web.service.auth_service import AuthService

api = Namespace("auth", description="Auth namespace")


@api.route("/login/")
class LoginController(Resource):
    @api.response(200, "Logged in successfully")
    @api.response(400, "Invalid request data")
    def post(self):
        login_data: AuthDTO = AuthSchema().load(request.json)
        AuthService.login(data=login_data)

        return Response(status=200)


@api.route("/logout/")
class LogoutController(Resource):
    @api.response(200, "Logged out successfully")
    def post(self):
        AuthService.logout()

        return Response(status=200)
