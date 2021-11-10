from enum import Enum

from flask_principal import Permission, RoleNeed


class Role(Enum):
    buyer = "buyer"
    seller = "seller"


buyer_permission = Permission(RoleNeed(Role.buyer.value))
seller_permission = Permission(RoleNeed(Role.seller.value))
