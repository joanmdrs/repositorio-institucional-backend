from django.db import models
from apps.trabalho.models import Trabalho

class Arquivo(models.Model):
    trabalho = models.ForeignKey(Trabalho, on_delete=models.CASCADE, related_name='arquivos')
    arquivo = models.FileField(upload_to='trabalhos/')
    nome = models.CharField(max_length=255, null=True, blank=True)
    tipo = models.CharField(max_length=50)
    tamanho = models.PositiveIntegerField()
    checksum = models.CharField(max_length=64)
    criado_em = models.DateTimeField(auto_now_add=True)