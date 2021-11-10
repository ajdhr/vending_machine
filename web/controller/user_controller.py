from flask import request, Response
from flask_restplus import Namespace, Resource

from web.dto.user_dto import UserDTO, GetUserDTO
from web.schema.user_schema import UserSchema, GetUserSchema
from web.service.user_service import UserService

api = Namespace("user", description="User namespace")


@api.route("/")
class CreateUserController(Resource):
    def post(self):
        user_data: UserDTO = UserSchema().load(request.json)
        UserService.create(data=user_data)

        return Response(status=201)


@api.route("/")
class UserController(Resource):
    def get(self):
        user_data: GetUserDTO = UserService.get()

        response_data = GetUserSchema().dump(user_data)

        return response_data, 200

    def put(self):
        user_data: UserDTO = UserSchema().load(request.json)
        UserService.update(data=user_data)

        return Response(status=201)

    def delete(self):
        UserService.delete()

        return Response(status=204)
