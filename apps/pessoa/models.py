from django.db import models
from apps.usuario.models import Usuario

class Pessoa(models.Model):
    TITULACAO_CHOICES = [
        ('GRAD', 'Graduação'),
        ('ESPE', 'Especialização'),
        ('MEST', 'Mestrado'),
        ('DOUT', 'Doutorado'),
        ('POSDOUT', 'Pós-Doutorado'),
    ]
    
    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="pessoa"
    )

    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(blank=True, null=True, max_length=11)
    titulacao_maxima = models.CharField(max_length=50, choices=TITULACAO_CHOICES, null=True, blank=True)   

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return self.nome

