from users.application.dtos import LoginDTO, RegisterDTO, VerifyMailDTO
from users.application.validations import validate_register_dto, validate_login_dto
from users.infrastructure.csrf import generate_csrf_token
from users.infrastructure.repositories import DjangoUserRepository
from users.infrastructure.email_service import EmailService
from users.models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


class UserService:
    def __init__(self, user_repository: DjangoUserRepository):
        self.user_repository = user_repository

    def login_user(self, request, login_dto: LoginDTO):
        error = validate_login_dto(login_dto)

        if error:
            return JsonResponse({"Error": error}, status=400)

        user = login_dto.username or login_dto.email
        user = self.user_repository.get_user(user)

        if not user:
            return JsonResponse({"error": "User not found"}, status=400)

        if login_dto.email and not login_dto.username:
            data_to_login = login_dto.email
        else:
            data_to_login = login_dto.username

        user = authenticate(
            request,
            username=data_to_login,
            password=login_dto.password
        )

        if (user):

            login(request, user)

            response = JsonResponse(
                {"message": "Login exitoso"},
                status=200
            )
            response["X-CRFToken"] = generate_csrf_token(request)

            return response

        return JsonResponse({"error": "Credenciales incorrect"}, status=400)

    def logout_user(self, request):

        logout(request)

        return JsonResponse({"message": "Logout success"}, status=400)

    def create(self, request, register_dto: RegisterDTO):

        error = validate_register_dto(register_dto)

        if error:
            return JsonResponse({"Error": error}, status=400)

        username = self.user_repository.get_user(register_dto.username)
        email = self.user_repository.get_email(register_dto.email)

        if username or email:
            return JsonResponse({"Error": "User exist"}, status=400)

        register_dto.token = CustomUser.generate_token(register_dto)

        try:

            self.user_repository.create_user(register_dto)
            EmailService.send_welcome_email(
                register_dto.email,
                register_dto.username,
                register_dto.token
            )
            return JsonResponse({"Success": "You user is now register check your email to activate your acount."})
        except Exception as e:
            print(e)
            return JsonResponse({"Error": "An error occurred while creating your user, please try again in a few minutes."})

    def verify_email(self, request, verify_email_dto: VerifyMailDTO):
        token = self.user_repository.check_email_token(verify_email_dto)

        if not token:
            return JsonResponse({"Error": "User not exist or token is invalid"}, status=400)
