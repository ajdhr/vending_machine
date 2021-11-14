class MockDepositData:
    @staticmethod
    def get_valid_deposit_data() -> dict:
        return {"amount": 10}

    @staticmethod
    def get_invalid_deposit_data() -> dict:
        return {"amount": -10}
