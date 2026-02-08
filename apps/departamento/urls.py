from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartamentoViewSet

router = DefaultRouter()
router.register(r'', DepartamentoViewSet, basename='departamento')

app_name = 'departamento'

urlpatterns = [
    path('', include(router.urls)),
]
