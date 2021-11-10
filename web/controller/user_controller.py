from flask import request, Response
from flask_restplus import Namespace, Resource

from web.dto.user_dto import CreateUserDTO
from web.schema.user_schema import CreateUserSchema
from web.service.user_service import UserService

api = Namespace("user", description="User namespace")


@api.route("/")
class UserController(Resource):
    def post(self):
        user_data: CreateUserDTO = CreateUserSchema().load(request.json)
        UserService.create(data=user_data)

        return Response(status=201)
