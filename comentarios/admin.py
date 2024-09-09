from django.contrib import admin
from .models import Comentario
# Register your models here.
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('publicacao', 'autor', 'conteudo', 'data_criacao')
    search_fields = ('autor',)
    list_filter = ('autor', 'data_criacao')