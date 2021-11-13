class MockUserData:
    @staticmethod
    def get_valid_create_user_request_data():
        return {
            "username": "testUser",
            "password": "test123",
            "role": "buyer",
        }

    @staticmethod
    def get_create_user_request_data_with_missing_field():
        return {
            "username": "testUser",
            "role": "buyer",
        }
