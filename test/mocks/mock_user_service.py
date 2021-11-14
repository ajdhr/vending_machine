from role import Role
from web.dto.user_dto import UserDTO, UserResponseDTO


class MockUserService:
    @classmethod
    def create(cls, data: UserDTO):
        return

    @classmethod
    def get(cls) -> UserResponseDTO:
        return UserResponseDTO(id=1, username="TestUser", role=Role.buyer, deposit=0)
