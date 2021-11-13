from werkzeug.exceptions import BadRequest, NotFound, Unauthorized, Forbidden


class InvalidUserCredentials(Unauthorized):
    def __init__(self):
        super().__init__("Invalid credentials provided")


class UserAlreadyExists(BadRequest):
    def __init__(self, username: str):
        super().__init__(f"User with username ({username}) already exists in the system")


class ProductNotFoundException(NotFound):
    def __init__(self, product_id: int):
        super().__init__(f"Product with ID({product_id}) does not exist")


class ProductNotOwnedByUser(Forbidden):
    def __init__(self, product_id: int):
        super().__init__(f"Current user does not own the product with ID({product_id})")


class InsufficientFunds(BadRequest):
    def __init__(self):
        super().__init__(f"Insufficient funds for the transaction")


class ProductQuantityUnavailable(BadRequest):
    def __init__(self):
        super().__init__(f"Requested product quantity unavailable")
