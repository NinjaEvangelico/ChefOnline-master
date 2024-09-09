from django.contrib.auth.models import User
from django.db import models

class Publicacao(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='fotos_receitas/')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)  # Atributo curtidas
    data_criacao = models.DateTimeField(auto_now_add=True)

    def curtir(self):
        """Incrementa o número de curtidas"""
        self.likes += 1
        self.save()

    def descurtir(self):
        """Decrementa o número de curtidas"""
        if self.likes > 0:
            self.likes -= 1
            self.save()

    def __str__(self):
        return self.titulo

