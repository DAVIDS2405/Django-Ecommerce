from drf_spectacular.utils import extend_schema
from rest_framework import status
from users.presentation.docs_serializers import LoginSerializer, RegisterSerializer, VerifyMailSerializer

UserLoginDocs = extend_schema(
    request=LoginSerializer,
    responses={status.HTTP_200_OK: dict, status.HTTP_400_BAD_REQUEST: dict},
    description="Endpoint para iniciar sesión de usuario.",
)

UserLogoutDocs = extend_schema(
    request=None,
    responses={status.HTTP_200_OK: dict},
    description="Endpoint para cerrar sesión de usuario.",
)

UserCreateDocs = extend_schema(
    request=RegisterSerializer,
    responses={status.HTTP_201_CREATED: dict,
               status.HTTP_400_BAD_REQUEST: dict},
    description="Endpoint para registrar un nuevo usuario.",
)

UserVerifyMailDocs = extend_schema(
    request=VerifyMailSerializer,
    responses={status.HTTP_200_OK: dict, status.HTTP_400_BAD_REQUEST: dict},
    description="Endpoint para verificar correo.",
)
