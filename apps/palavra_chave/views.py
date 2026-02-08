from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from core.pagination import DefaultPagination
from apps.palavra_chave.models import PalavraChave
from .serializers import PalavraChaveSerializer
from rest_framework.permissions import AllowAny

class PalavraChaveViewSet(ModelViewSet):
    queryset = PalavraChave.objects.all().order_by("id")
    permission_classes = [AllowAny]
    serializer_class = PalavraChaveSerializer
    pagination_class = DefaultPagination
    filter_backends = [SearchFilter]
    search_fields = ['termo']
