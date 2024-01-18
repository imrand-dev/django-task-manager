from django.urls import path

from account.views import PublicUserRegistration

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("/signup", PublicUserRegistration.as_view(), name="user-signup"),
    path("/login", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("/api/token-refresh", TokenRefreshView.as_view(), name="token-refresh"),
]