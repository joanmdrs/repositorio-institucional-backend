from rest_framework.serializers import ModelSerializer
from apps.palavra_chave.models import PalavraChave

class PalavraChaveSerializer(ModelSerializer):
    class Meta:
        model = PalavraChave
        fields = '__all__'  