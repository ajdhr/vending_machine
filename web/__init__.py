from flask import Blueprint
from flask_restplus import Api

from .controller.user_controller import api as user_ns

blueprint = Blueprint("api", __name__)

api = Api(
    blueprint,
    title="Vending machine",
    version="1.0",
    description="A vending machine api",
    prefix="/api",
    catch_all_404s=True,
)

api.add_namespace(user_ns)
