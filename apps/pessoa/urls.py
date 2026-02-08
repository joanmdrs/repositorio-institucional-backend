from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PessoaViewSet

router = DefaultRouter()
router.register(r'', PessoaViewSet, basename='pessoa')

app_name = 'pessoa'

urlpatterns = [
    path('', include(router.urls)),
]
