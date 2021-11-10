from dataclasses import dataclass

from role import Role


@dataclass
class UserDTO:
    username: str
    password: str
    role: Role


@dataclass
class UserResponseDTO:
    username: str
    role: Role
    deposit: int
