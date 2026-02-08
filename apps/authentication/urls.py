from django.urls import path
from apps.authentication.token.custom_token import CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'auth'
urlpatterns = [
    path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
