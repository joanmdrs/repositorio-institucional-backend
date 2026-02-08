from django.contrib import admin
from apps.curso.models import Curso

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nivel', 'descricao', 'departamento')
    search_fields = ('nome', 'nivel', 'departamento__nome')  
    list_filter = ('departamento', 'nivel')
    
admin.site.register(Curso, CursoAdmin)