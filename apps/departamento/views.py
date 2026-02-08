from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from core.pagination import DefaultPagination
from apps.curso.models import Departamento
from .serializers import DepartamentoSerializer
from rest_framework.permissions import AllowAny

class DepartamentoViewSet(ModelViewSet):
    queryset = Departamento.objects.all().order_by("id")
    permission_classes = [AllowAny]
    serializer_class = DepartamentoSerializer
    pagination_class = DefaultPagination
    filter_backends = [SearchFilter]
    search_fields = ['nome', 'sigla']
