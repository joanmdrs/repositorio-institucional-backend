from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, GroupViewSet

router = DefaultRouter()
router.register(r'', UsuarioViewSet, basename='usuario')

app_name = 'usuario'

urlpatterns = [
    path('', include(router.urls)),
]
