from dataclasses import dataclass


@dataclass
class AuthDTO:
    username: str
    password: str
