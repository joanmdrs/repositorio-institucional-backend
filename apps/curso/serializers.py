from rest_framework.serializers import ModelSerializer, CharField
from apps.curso.models import Curso

class CursoSerializer(ModelSerializer):
    departamento_nome = CharField(source='departamento.nome', read_only=True)
    
    class Meta:
        model = Curso
        fields = '__all__'

        