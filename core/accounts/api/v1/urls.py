from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import CustomAuthToken, DiscardAuthToken

app_name = "api-v1"

urlpatterns = [
    path("jwt/create", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("jwt/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("jwt/verify", TokenVerifyView.as_view(), name="token_verify"),
    path("token/login", CustomAuthToken.as_view(), name="token_login"),
    path("token/logout", DiscardAuthToken.as_view(), name="token_logout"),
]
