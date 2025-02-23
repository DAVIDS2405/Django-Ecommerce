from django.middleware.csrf import get_token


def generate_csrf_token(request):
    """Genera un token CSRF para la sesión actual"""
    return get_token(request)
