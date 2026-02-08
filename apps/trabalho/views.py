import hashlib

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import status

from .models import Trabalho
from .serializers import TrabalhoReadSerializer, TrabalhoWriteSerializer
from apps.arquivo.models import Arquivo
from core.pagination import DefaultPagination


class TrabalhoViewSet(ModelViewSet):
    queryset = Trabalho.objects.all().order_by("id")
    permission_classes = [AllowAny]
    pagination_class = DefaultPagination
    parser_classes = [MultiPartParser, FormParser]
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return TrabalhoReadSerializer
        return TrabalhoWriteSerializer

    filter_backends = [SearchFilter]
    search_fields = ["titulo", "ano_defesa"]

    def perform_create(self, serializer):
        trabalho = serializer.save()
        self._salvar_arquivo(trabalho)

    def perform_update(self, serializer):
        trabalho = serializer.save()
        self._salvar_arquivo(trabalho)

    def _salvar_arquivo(self, trabalho):
        arquivo_file = self.request.FILES.get("arquivo")

        if not arquivo_file:
            return

        hash_sha256 = hashlib.sha256()
        for chunk in arquivo_file.chunks():
            hash_sha256.update(chunk)

        Arquivo.objects.create(
            trabalho=trabalho,
            arquivo=arquivo_file,
            nome=arquivo_file.name,
            tipo=arquivo_file.content_type,
            tamanho=arquivo_file.size,
            checksum=hash_sha256.hexdigest()
        )
