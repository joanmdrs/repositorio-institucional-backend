from rest_framework import serializers
from django.contrib.auth.models import Group
from apps.usuario.models import Usuario
from .models import Pessoa
from .utils.masks import mask_cpf, mask_telefone

class PessoaReadSerializer(serializers.ModelSerializer):
    usuario_id = serializers.IntegerField(source='usuario.id', read_only=True)
    username = serializers.CharField(source='usuario.username', read_only=True)
    email = serializers.EmailField(source='usuario.email', read_only=True)

    groups = serializers.SlugRelatedField(
        source='usuario.groups',
        many=True,
        read_only=True,
        slug_field='id'
    )

    titulacao_nome = serializers.CharField(
        source='get_titulacao_maxima_display',
        read_only=True
    )

    cpf = serializers.SerializerMethodField()
    telefone = serializers.SerializerMethodField()

    class Meta:
        model = Pessoa
        fields = [
            'id',
            'nome',
            'cpf',
            'telefone',
            'titulacao_maxima',
            'titulacao_nome',
            'usuario_id',
            'username',
            'email',
            'groups',
        ]

    def get_cpf(self, obj):
        return mask_cpf(obj.cpf)

    def get_telefone(self, obj):
        return mask_telefone(obj.telefone)
    

class PessoaWriteSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True, required=False)

    groups = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Group.objects.all(),
        write_only=True,
        required=False
    )

    class Meta:
        model = Pessoa
        fields = [
            'nome',
            'cpf',
            'telefone',
            'titulacao_maxima',
            'username',
            'email',
            'password',
            'groups',
        ]

    # ================= CREATE =================
    def create(self, validated_data):
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        password = validated_data.pop('password', None)
        groups = validated_data.pop('groups', [])

        usuario = Usuario.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        if groups:
            usuario.groups.set(groups)

        pessoa = Pessoa.objects.create(
            usuario=usuario,
            email=email,
            **validated_data
        )

        return pessoa

    # ================= UPDATE =================
    def update(self, instance, validated_data):
        usuario = instance.usuario

        if 'username' in validated_data:
            usuario.username = validated_data.pop('username')

        if 'email' in validated_data:
            usuario.email = validated_data.pop('email')

        if 'password' in validated_data:
            usuario.set_password(validated_data.pop('password'))

        if 'groups' in validated_data:
            usuario.groups.set(validated_data.pop('groups'))

        usuario.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

