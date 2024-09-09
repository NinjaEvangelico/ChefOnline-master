from django.contrib import admin
from .models import Publicacao
# Register your models here.
@admin.register(Publicacao)
class PublicacaoAdmin(admin.ModelAdmin):      
    list_display = ('titulo','descricao','autor','foto','data_criacao','likes')
    search_fields = ('autor','titulo')
    list_filter = ('autor','titulo')