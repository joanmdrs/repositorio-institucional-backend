from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from core.pagination import DefaultPagination
from apps.usuario.models import Usuario
from django.contrib.auth.models import Group
from .serializers import UsuarioWriteSerializer, UsuarioReadSerializer, GroupSerializer
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all().order_by("id")
    permission_classes = [AllowAny]
    pagination_class = DefaultPagination
    filter_backends = [SearchFilter]
    search_fields = ['username']
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return UsuarioReadSerializer
        return UsuarioWriteSerializer

class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [AllowAny]