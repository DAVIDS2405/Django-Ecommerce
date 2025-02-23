from abc import ABC, abstractmethod
from typing import Optional
from users.application.dtos import RegisterDTO, VerifyMailDTO
from users.models import CustomUser


class UserRepositoryInterface(ABC):
    """Interfaz para el repositorio de usuarios"""

    @abstractmethod
    def get_user(username: Optional[str] = None, email: Optional[str] = None) -> str:
        pass

    @abstractmethod
    def get_email(self, email: str) -> str:
        pass

    @abstractmethod
    def create_user(self, register_dto: RegisterDTO) -> CustomUser:
        pass

    @abstractmethod
    def check_email_token(self, very_mail_dtp: VerifyMailDTO) -> str:
        pass
