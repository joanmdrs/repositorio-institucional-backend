from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter

from .models import Pessoa
from .serializers import PessoaReadSerializer, PessoaWriteSerializer
from core.pagination import DefaultPagination


class PessoaViewSet(ModelViewSet):
    queryset = Pessoa.objects.all().order_by('id')
    permission_classes = [AllowAny]
    pagination_class = DefaultPagination

    filter_backends = [SearchFilter]
    search_fields = [
        'nome',
        'cpf'
    ]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return PessoaReadSerializer
        return PessoaWriteSerializer
