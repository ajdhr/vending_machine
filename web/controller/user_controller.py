from flask import request, Response
from flask_login import login_required
from flask_restplus import Namespace, Resource

from web.dto.user_dto import UserDTO, UserResponseDTO
from web.schema.user_schema import UserSchema, UserResponseSchema
from web.service.user_service import UserService
from web.utils.validation_error_handler import validation_error_handler

api = Namespace("user", description="User namespace")


@api.route("/")
class CreateUserController(Resource):
    @validation_error_handler
    @api.response(201, "User successfully created")
    @api.response(400, "Invalid request data")
    def post(self):
        user_data: UserDTO = UserSchema().load(request.json)
        UserService.create(data=user_data)

        return Response(status=201)


@api.route("/")
class UserController(Resource):
    @login_required
    @api.response(200, "User successfully retrieved")
    @api.response(401, "Unauthorized access")
    def get(self):
        user_data: UserResponseDTO = UserService.get()

        response_data = UserResponseSchema().dump(user_data)

        return response_data, 200

    @login_required
    @validation_error_handler
    @api.response(200, "User successfully updated")
    @api.response(400, "Invalid request data")
    @api.response(401, "Unauthorized access")
    def put(self):
        user_data: UserDTO = UserSchema().load(request.json)
        UserService.update(data=user_data)

        return Response(status=201)

    @login_required
    @api.response(204, "User successfully deleted")
    @api.response(401, "Unauthorized access")
    def delete(self):
        UserService.delete()

        return Response(status=204)
