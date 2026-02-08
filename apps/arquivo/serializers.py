from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apps.arquivo.models import Arquivo

class ArquivoSerializer(ModelSerializer):
    trabalho_titulo = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Arquivo
        fields = [
            "id",
            "nome",
            "arquivo",
            "tipo",
            "tamanho",
            "checksum",
            "trabalho",
            "trabalho_titulo",
            "criado_em",
        ]

    def get_trabalho_titulo(self, obj):
        return obj.trabalho.titulo if obj.trabalho else None
