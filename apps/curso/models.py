from django.db import models
from apps.departamento.models import Departamento

class Curso(models.Model):
    
    NIVEL_CHOICES = [   
        ('graduacao', 'Graduação'),
        ('pos_graduacao', 'Pós-Graduação'), 
        ('tecnico', 'Técnico'),
    ]
    
    nome = models.CharField(max_length=255)
    sigla = models.CharField(max_length=20)
    nivel = models.CharField(max_length=50, choices=NIVEL_CHOICES)
    descricao = models.TextField(blank=True, null=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
    def __unicode__(self):
        return self.nome    