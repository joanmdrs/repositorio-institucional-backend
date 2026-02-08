from django.contrib import admin
from apps.palavra_chave.models import PalavraChave

class PalavraChaveAdmin(admin.ModelAdmin):
    list_display = ('termo',)
    search_fields = ('termo',)  
    
admin.site.register(PalavraChave, PalavraChaveAdmin)