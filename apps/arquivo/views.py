from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import FileResponse
from core.pagination import DefaultPagination
import hashlib

from .models import Arquivo
from .serializers import ArquivoSerializer


class ArquivoViewSet(ModelViewSet):
    queryset = Arquivo.objects.all().order_by("-criado_em")
    serializer_class = ArquivoSerializer
    permission_classes = [AllowAny]
    pagination_class = DefaultPagination
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        file = self.request.FILES.get("arquivo")

        if file:
            checksum = hashlib.sha256(file.read()).hexdigest()
            file.seek(0)

            serializer.save(
                nome=file.name,
                tipo=file.content_type,
                tamanho=file.size,
                checksum=checksum,
            )
        else:
            serializer.save()

    @action(detail=True, methods=["get"], url_path="download")
    def download(self, request, pk=None):
        arquivo = self.get_object()
        return FileResponse(
            arquivo.arquivo.open(),
            as_attachment=True,
            filename=arquivo.nome
        )
