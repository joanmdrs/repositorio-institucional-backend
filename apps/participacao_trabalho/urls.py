from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParticipacaoTrabalhoViewSet

router = DefaultRouter()
router.register(r'', ParticipacaoTrabalhoViewSet, basename='participacao_trabalho')

app_name = 'participacao_trabalho'

urlpatterns = [
    path('', include(router.urls)),
]
