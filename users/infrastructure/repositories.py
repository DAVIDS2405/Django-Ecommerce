from typing import Optional
from users.application.dtos import RegisterDTO, VerifyMailDTO
from users.domain.interfaces import UserRepositoryInterface
from users.models import CustomUser
from django.contrib.auth import get_user_model

Users = get_user_model()


class DjangoUserRepository(UserRepositoryInterface):
    """Implementación del repositorio con Django ORM"""

    def get_user(username: Optional[str] = None, email: Optional[str] = None) -> str:
        if username:
            return Users.objects.filter(username=username).all()
        elif email:
            return Users.objects.filter(email=email).all()
        return None

    def get_email(self, email: str) -> str:
        return Users.objects.filter(email=email).first()

    def create_user(self, register_dto: RegisterDTO) -> CustomUser:
        return Users.objects.create_user(**register_dto.__dict__)

    def check_email_token(self, very_mail_dtp: VerifyMailDTO) -> bool:
        return Users.objects.filter(token=very_mail_dtp.token, email=very_mail_dtp.email).first()
