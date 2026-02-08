from django.contrib import admin
from apps.departamento.models import Departamento

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo', 'descricao')
    search_fields = ('nome', 'codigo')  
    
admin.site.register(Departamento, DepartamentoAdmin)