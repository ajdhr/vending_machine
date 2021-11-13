from typing import List

from flask import request, Response
from flask_login import login_required
from flask_restplus import Resource, Namespace

from role import seller_permission
from web.dto.product_dto import ProductDTO, ProductResponseDTO
from web.schema.product_schema import ProductSchema, ProductResponseSchema
from web.service.product_service import ProductService
from web.utils.validation_error_handler import validation_error_handler

api = Namespace("product", description="Product namespace")


@api.route("/")
class ProductListController(Resource):
    @login_required
    @seller_permission.require(http_exception=403)
    @validation_error_handler
    def post(self):
        product_data: ProductDTO = ProductSchema().load(request.json)
        product_response_data: ProductResponseDTO = ProductService.create(data=product_data)

        response = ProductResponseSchema().dump(product_response_data)
        return response, 201

    @login_required
    def get(self):
        products_data: List[ProductResponseDTO] = ProductService.get_all()
        response = ProductResponseSchema(many=True).dump(products_data)

        return response, 200


@api.route("/<int:id>/")
class ProductController(Resource):
    @login_required
    def get(self, id):
        product_data: ProductResponseDTO = ProductService.get(product_id=id)
        response = ProductResponseSchema().dump(product_data)

        return response, 200

    @login_required
    @seller_permission.require(http_exception=403)
    @validation_error_handler
    def put(self, id):
        product_data: ProductDTO = ProductSchema().load(request.json)

        product_response_data: ProductResponseDTO = ProductService.update(product_id=id, data=product_data)

        response = ProductResponseSchema().dump(product_response_data)
        return response, 201

    @login_required
    @seller_permission.require(http_exception=403)
    def delete(self, id):
        ProductService.delete(product_id=id)

        return Response(status=204)
