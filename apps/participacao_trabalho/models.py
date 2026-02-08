from django.db import models
from apps.trabalho.models import Trabalho
from apps.pessoa.models import Pessoa

class ParticipacaoTrabalho(models.Model):
    PAPEL_CHOICES = [
        ('AUTOR', 'Autor'),
        ('ORIENTADOR', 'Orientador'),
        ('COORIENTADOR', 'Coorientador'),
    ]

    trabalho = models.ForeignKey(
        Trabalho,
        on_delete=models.CASCADE,
        related_name='participacoes'
    )

    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.PROTECT,
        related_name='participacoes'
    )

    papel = models.CharField(max_length=20, choices=PAPEL_CHOICES)

    ordem_autoria = models.PositiveIntegerField(null=True, blank=True)
