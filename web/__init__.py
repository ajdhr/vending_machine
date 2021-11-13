from flask import Blueprint
from flask_restplus import Api

from .controller.user_controller import api as user_ns
from .controller.auth_controller import api as auth_ns
from .controller.product_controller import api as product_ns
from .controller.deposit_controller import api as deposit_ns
from .controller.reset_controller import api as reset_ns
from .controller.buy_controller import api as buy_ns

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
api.add_namespace(auth_ns)
api.add_namespace(product_ns)
api.add_namespace(deposit_ns)
api.add_namespace(reset_ns)
api.add_namespace(buy_ns)
