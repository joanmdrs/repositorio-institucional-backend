from django.db import models
from apps.curso.models import Curso
from apps.palavra_chave.models import PalavraChave

class Trabalho(models.Model):
    TIPO_CHOICES = [
        ('ART', 'Artigo'),
        ('MON', 'Monografia'),
        ('DIS', 'Dissertação'),
        ('TES', 'Tese'),
    ]

    titulo = models.CharField(max_length=500)
    resumo = models.TextField(blank=True, null=True)
    abstract = models.TextField(blank=True, null=True)
    ano_defesa = models.PositiveIntegerField()
    data_defesa = models.DateField()

    tipo = models.CharField(max_length=3, choices=TIPO_CHOICES)
    idioma = models.CharField(max_length=50)
    disponivel_consulta = models.BooleanField(default=True)

    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    editor = models.CharField(max_length=255, blank=True, null=True)

    palavras_chave = models.ManyToManyField(PalavraChave)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
