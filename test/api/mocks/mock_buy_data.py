class MockBuyData:
    @staticmethod
    def get_valid_buy_request_data() -> dict:
        return {"product_id": 1, "amount": 1}

    @staticmethod
    def get_buy_request_data_with_invalid_amount() -> dict:
        return {"product_id": 1, "amount": -1}
