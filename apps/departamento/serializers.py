from rest_framework.serializers import ModelSerializer
from apps.departamento.models import Departamento

class DepartamentoSerializer(ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'  