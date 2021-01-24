from django.contrib import admin
from .models import Receita

# Register your models here.

class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'tempo_preparo', 'publicada')
    list_display_links = ('id', 'nome_receita')
    list_editable = ('publicada',)
    search_fields = ('nome_receitas',) # tem que ser uma tupla
    list_filter = ('categoria',) # tem que ser uma tupla
    list_per_page = 10
    

admin.site.register(Receita, ListandoReceitas)

