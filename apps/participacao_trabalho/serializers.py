from rest_framework.serializers import ModelSerializer, IntegerField, CharField
from .models import ParticipacaoTrabalho

class ParticipacaoTrabalhoSerializer(ModelSerializer):
    titulo_trabalho = CharField(source='trabalho.titulo', read_only=True)
    nome_pessoa = CharField(source='pessoa.nome', read_only=True)
    nome_papel = CharField(
        source='get_papel_display',
        read_only=True
    )
    
    class Meta:
        model = ParticipacaoTrabalho
        fields = ['id', 'trabalho', 'titulo_trabalho', 'pessoa', 'nome_pessoa', 'papel', 'nome_papel']