from rest_framework.decorators import api_view, permission_classes
from users.application.dtos import LoginDTO, RegisterDTO, VerifyMailDTO
from users.infrastructure.authentication import UserService
from users.infrastructure.repositories import DjangoUserRepository
from django_ratelimit.decorators import ratelimit
from users.presentation.docs import UserLoginDocs, UserLogoutDocs, UserCreateDocs, UserVerifyMailDocs
from rest_framework.permissions import AllowAny


user_repository = DjangoUserRepository()
auth_service = UserService(user_repository)


@UserLoginDocs
@api_view(["POST"])
@permission_classes([AllowAny])
@ratelimit(key='ip', rate='5/m', method='POST')
def UserLoginView(request):
    login_dto = LoginDTO(
        username=request.data.get("username"),
        password=request.data.get("password"),
        email=request.data.get("email")

    )
    return auth_service.login_user(request, login_dto)


@UserLogoutDocs
@api_view(["POST"])
@permission_classes([AllowAny])
@ratelimit(key='ip', rate='5/m', method='POST')
def UserLogoutView(request):
    return auth_service.logout_user(request)


@UserCreateDocs
@api_view(["POST"])
@permission_classes([AllowAny])
@ratelimit(key='ip', rate='5/m', method='POST')
def UserCreateView(request):
    register_dto = RegisterDTO(
        username=request.data.get("username"),
        password=request.data.get("password"),
        address=request.data.get("address"),
        ci=request.data.get("ci"),
        phone_number=request.data.get("ci"),
        email=request.data.get("email")

    )
    return auth_service.create(request, register_dto)


@UserVerifyMailDocs
@api_view(["POST"])
@permission_classes([AllowAny])
@ratelimit(key='ip', rate='5/m', method='POST')
def UserVerifyMailView(request, token):
    verify_email_dto = VerifyMailDTO(
        token=token,
        email=request.data.get("email")

    )
    return auth_service.verify_email(request, verify_email_dto)
