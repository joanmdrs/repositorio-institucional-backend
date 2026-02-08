from django.contrib import admin
from apps.trabalho.models import Trabalho

class TrabalhoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_defesa', 'curso')
    search_fields = ('titulo', 'curso__nome')
    list_filter = ('data_defesa', 'curso', 'ano_defesa', 'tipo')  
    
admin.site.register(Trabalho, TrabalhoAdmin)