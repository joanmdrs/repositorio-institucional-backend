from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from core.pagination import DefaultPagination
from apps.curso.models import Curso
from .serializers import CursoSerializer
from rest_framework.permissions import AllowAny

class CursoViewSet(ModelViewSet):
    queryset = Curso.objects.all().order_by("id")
    permission_classes = [AllowAny]
    serializer_class = CursoSerializer
    pagination_class = DefaultPagination
    filter_backends = [SearchFilter]
    search_fields = ['nome', 'codigo']
