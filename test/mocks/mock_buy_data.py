class MockBuyData:
    @staticmethod
    def get_valid_buy_request_data() -> dict:
        return MockBuyData.get_buy_request_data(product_id=1, amount=1)

    @staticmethod
    def get_buy_request_data_with_invalid_amount() -> dict:
        return {"product_id": 1, "amount": -1}

    @staticmethod
    def get_buy_request_data(product_id: int, amount: int) -> dict:
        return {"product_id": product_id, "amount": amount}
