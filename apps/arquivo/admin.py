from django.contrib import admin
from apps.arquivo.models import Arquivo 

class ArquivoAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'nome', 'trabalho', 'tipo', 'tamanho', 'criado_em')
    search_fields = ('trabalho__titulo', 'tipo')
    list_filter = ('tipo', 'criado_em')
    
admin.site.register(Arquivo, ArquivoAdmin)