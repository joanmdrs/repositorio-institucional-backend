from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArquivoViewSet

router = DefaultRouter()
router.register(r'', ArquivoViewSet, basename='arquivo')

app_name = 'arquivo'

urlpatterns = [
    path('', include(router.urls)),
]
