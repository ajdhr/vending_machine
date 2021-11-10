class InvalidUserCredentials(Exception):
    def __init__(self):
        super().__init__("Invalid credentials provided")


class ProductNotFoundException(Exception):
    def __init__(self, product_id: int):
        super().__init__(f"Product with ID({product_id}) does not exist")


class ProductNotOwnedByUser(Exception):
    def __init__(self, product_id: int):
        super().__init__(f"Current user does not own the product with ID({product_id})")

