from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from core.pagination import DefaultPagination
from apps.participacao_trabalho.models import ParticipacaoTrabalho
from .serializers import ParticipacaoTrabalhoSerializer
from rest_framework.permissions import AllowAny

class ParticipacaoTrabalhoViewSet(ModelViewSet):
    queryset = ParticipacaoTrabalho.objects.all().order_by("id")
    permission_classes = [AllowAny]
    serializer_class = ParticipacaoTrabalhoSerializer
    pagination_class = DefaultPagination
    # filter_backends = [SearchFilter]
    # search_fields = ['username']
