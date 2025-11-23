from django.contrib import admin
from .models import Anuncio, Foto

@admin.register(Anuncio)
class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'marca', 'modelo', 'ano', 'preco', 'criado_em')
    search_fields = ('marca', 'modelo', 'owner__username')

@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'anuncio', 'ordem', 'imagem')
    list_filter = ('anuncio',)