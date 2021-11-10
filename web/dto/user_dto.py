from dataclasses import dataclass

from role import Role


@dataclass
class CreateUserDTO:
    username: str
    password: str
    role: Role
