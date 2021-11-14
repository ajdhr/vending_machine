class MockProductData:
    @staticmethod
    def get_valid_product_request_data() -> dict:
        return {"name": "testProduct", "cost": 1, "amount_available": 3}
