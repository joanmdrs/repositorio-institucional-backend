from django.db import models

class Departamento(models.Model):
    nome = models.CharField(max_length=255)
    sigla = models.CharField(max_length=10, unique=True, null=True, blank=True)
    codigo = models.CharField(max_length=10, unique=True, null=True, blank=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return self.nome