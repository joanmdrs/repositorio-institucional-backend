
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from apps.pessoa.models import Pessoa

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        pessoa = None
        try:
            pessoa = self.user.pessoa
        except Pessoa.DoesNotExist:
            pass

        groups = list(self.user.groups.values_list("name", flat=True))

        data["user"] = {
            "id_usuario": self.user.id,
            "id_pessoa": pessoa.id if pessoa else None,
            "nome": pessoa.nome if pessoa else self.user.username,
            "email": pessoa.email if pessoa else None,
            "groups": groups,
            "active_group": None,
        }

        return data

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
