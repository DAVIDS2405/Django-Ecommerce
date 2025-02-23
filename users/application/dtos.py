from dataclasses import dataclass
from typing import Optional


@dataclass
class LoginDTO:
    username: Optional[str] = None
    password: str = None
    email: Optional[str] = None


@dataclass
class RegisterDTO:
    username: Optional[str] = None
    password: str = None
    phone_number: str = None
    address: str = None
    ci: str = None
    email: Optional[str] = None


@dataclass
class VerifyMailDTO:
    token: str
    email: str
