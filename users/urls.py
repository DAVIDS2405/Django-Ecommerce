from django.urls import path
from users.presentation.views import UserLoginView, UserLogoutView, UserCreateView, UserVerifyMailView

urlpatterns = [
    path('login/', UserLoginView, name="login"),
    path('logout/', UserLogoutView, name="logout"),
    path('register/', UserCreateView, name='create'),
    path('verify-email/<str:token>', UserVerifyMailView, name='verify-email')
]
