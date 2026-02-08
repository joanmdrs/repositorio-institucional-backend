from rest_framework import serializers
from .models import Trabalho
from apps.arquivo.models import Arquivo
from apps.palavra_chave.models import PalavraChave
from apps.arquivo.serializers import ArquivoSerializer
from apps.participacao_trabalho.models import ParticipacaoTrabalho
import hashlib
import json

class PalavraChaveListField(serializers.Field):
    def to_internal_value(self, data):
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except json.JSONDecodeError:
                raise serializers.ValidationError("Formato inválido")

        if not isinstance(data, list):
            raise serializers.ValidationError("Esperado uma lista")

        palavras = []
        for termo in data:
            termo_normalizado = termo.strip().lower()
            palavra, _ = PalavraChave.objects.get_or_create(
                termo=termo_normalizado
            )
            palavras.append(palavra)

        return palavras

    def to_representation(self, value):
        return [p.termo for p in value.all()]



class TrabalhoBaseSerializer(serializers.ModelSerializer):
    palavras_chave = PalavraChaveListField(required=False)

    ano_defesa = serializers.IntegerField(read_only=True)

    class Meta:
        model = Trabalho
        fields = '__all__'

        
class TrabalhoReadSerializer(TrabalhoBaseSerializer):
    arquivos = ArquivoSerializer(many=True, read_only=True)
    autores = serializers.SerializerMethodField()
    orientadores = serializers.SerializerMethodField()
    coorientadores = serializers.SerializerMethodField()
    
    def _get_participacoes(self, obj, papel):
        qs = obj.participacoes.filter(papel=papel)

        return [
            {
                "id": p.pessoa.id,
                "nome": p.pessoa.nome
            }
            for p in qs
        ]
    
    def get_autores(self, obj):
        return self._get_participacoes(obj, 'AUTOR')

    def get_orientadores(self, obj):
        return self._get_participacoes(obj, 'ORIENTADOR')

    def get_coorientadores(self, obj):
        return self._get_participacoes(obj, 'COORIENTADOR')

class TrabalhoWriteSerializer(TrabalhoBaseSerializer):
    arquivo = serializers.FileField(required=False, write_only=True)
    autores = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=False
    )
    orientadores = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=False
    )
    coorientadores = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=False
    )

    def create(self, validated_data):
        palavras = validated_data.pop('palavras_chave', [])
        arquivo_file = validated_data.pop('arquivo', None)
        autores = validated_data.pop('autores', [])
        orientadores = validated_data.pop('orientadores', [])
        coorientadores = validated_data.pop('coorientadores', [])

        data_defesa = validated_data.get('data_defesa')
        if data_defesa:
            validated_data['ano_defesa'] = data_defesa.year

        trabalho = Trabalho.objects.create(**validated_data)
        trabalho.palavras_chave.set(palavras)
        self._criar_participacoes(trabalho, autores, orientadores, coorientadores)

        if arquivo_file:
            self._criar_arquivo(trabalho, arquivo_file)

        return trabalho

    def update(self, instance, validated_data):
        palavras = validated_data.pop('palavras_chave', None)
        arquivo_file = validated_data.pop('arquivo', None)
        autores = validated_data.pop('autores', [])
        orientadores = validated_data.pop('orientadores', [])
        coorientadores = validated_data.pop('coorientadores', [])

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if instance.data_defesa:
            instance.ano_defesa = instance.data_defesa.year

        instance.save()

        if palavras is not None:
            instance.palavras_chave.set(palavras)
            
        # Se vier qualquer lista de participação, recria tudo
        if autores is not None or orientadores is not None or coorientadores is not None:
            instance.participacoes.all().delete()
            self._criar_participacoes(
                instance,
                autores or [],
                orientadores or [],
                coorientadores or []
            )

        if arquivo_file:
            self._criar_arquivo(instance, arquivo_file)

        return instance
    
    def _criar_participacoes(self, trabalho, autores, orientadores, coorientadores):
        # Autores (com ordem)
        for index, pessoa_id in enumerate(autores):
            ParticipacaoTrabalho.objects.create(
                trabalho=trabalho,
                pessoa_id=pessoa_id,
                papel='AUTOR',
                ordem_autoria=index + 1
            )

        # Orientadores
        for pessoa_id in orientadores:
            ParticipacaoTrabalho.objects.create(
                trabalho=trabalho,
                pessoa_id=pessoa_id,
                papel='ORIENTADOR'
            )

        # Coorientadores
        for pessoa_id in coorientadores:
            ParticipacaoTrabalho.objects.create(
                trabalho=trabalho,
                pessoa_id=pessoa_id,
                papel='COORIENTADOR'
            )

    def _criar_arquivo(self, trabalho, arquivo_file):
        hash_sha256 = hashlib.sha256()
        for chunk in arquivo_file.chunks():
            hash_sha256.update(chunk)
        checksum = hash_sha256.hexdigest()

        Arquivo.objects.create(
            trabalho=trabalho,
            arquivo=arquivo_file,
            nome=arquivo_file.name,
            tipo=arquivo_file.content_type,
            tamanho=arquivo_file.size,
            checksum=checksum
        )
