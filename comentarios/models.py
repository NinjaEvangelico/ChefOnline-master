# comentarios/models.py
from django.contrib.auth.models import User
from django.db import models
from publicacoes.models import Publicacao

class Comentario(models.Model):
    publicacao = models.ForeignKey(Publicacao, related_name='comentarios', on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentário de {self.autor} em {self.publicacao}'
