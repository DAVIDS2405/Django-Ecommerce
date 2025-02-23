from typing import List
from users.application.dtos import RegisterDTO, LoginDTO
import re


def validate_login_dto(login_dto: LoginDTO) -> List[dict]:
    errors = []
    if not login_dto.username and not login_dto.email:
        errors.append({"field": "username or email",
                      "error": "This field is required"})

    if not login_dto.password:
        errors.append(
            {"field": "password", "error": "This field is required"})


def validate_register_dto(register_dto: RegisterDTO) -> List[dict]:
    errors = []

    if not register_dto.username:
        errors.append(
            {"field": "username", "error": "This field is required"})
    if not register_dto.password:
        errors.append(
            {"field": "password", "error": "This field is required"})

    elif not validate_password(register_dto.password):
        errors.append({"field": "password", "error": "Password must be 8-25 characters long and include at least one uppercase letter, one lowercase letter, one number, and one special character"})

    if not register_dto.phone_number:
        errors.append(
            {"field": "phone_number", "error": "This field is required"})
    if not register_dto.address:
        errors.append(
            {"field": "address", "error": "This field is required"})
    if not register_dto.ci:
        errors.append({"field": "ci", "error": "This field is required"})

    if not register_dto.email:
        errors.append({"field": "email", "error": "This field is required"})
    elif not validate_email(register_dto.email):
        errors.append({"field": "email", "error": "Invalid email format"})

    return errors


def validate_email(email: str) -> bool:
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return re.match(email_regex, email) is not None


def validate_password(password: str) -> bool:
    password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,25}$"
    return re.match(password_regex, password) is not None
