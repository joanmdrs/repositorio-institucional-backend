from django.contrib import admin
from .models import ParticipacaoTrabalho

class ParticipacaoTrabalhoAdmin(admin.ModelAdmin):
    list_display = ('id', 'trabalho', 'pessoa', 'papel', 'ordem_autoria')

admin.site.register(ParticipacaoTrabalho, ParticipacaoTrabalhoAdmin)
