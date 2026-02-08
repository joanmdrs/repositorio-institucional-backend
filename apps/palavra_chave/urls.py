from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PalavraChaveViewSet

router = DefaultRouter()
router.register(r'', PalavraChaveViewSet, basename='palavra_chave')

app_name = 'palavra_chave'

urlpatterns = [
    path('', include(router.urls)),
]
