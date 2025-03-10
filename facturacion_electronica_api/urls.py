"""
URL configuration for facturacion_electronica_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path
from django.views.generic import RedirectView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from dotenv import load_dotenv
import os


load_dotenv()
API_VERSION = os.getenv("API_VERSION")


def health_check(request):
    return JsonResponse({"status": "Server is running"}, status=200)


urlpatterns = [
    path("", RedirectView.as_view(
        url=f"{API_VERSION}/redoc/", permanent=True)),

    path(f"{API_VERSION}/schema/", SpectacularAPIView.as_view(),
         name="schema"),

    path(f"{API_VERSION}/swagger/",
         SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
    path(f"{API_VERSION}/redoc/",
         SpectacularRedocView.as_view(url_name="schema"), name="redoc"),

    path(f'{API_VERSION}/admin/', admin.site.urls),
    path(f"{API_VERSION}/", include('users.urls')),
]
