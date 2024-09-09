# comentarios/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Comentario
from publicacoes.models import Publicacao

def comentar_publicacao(request, publicacao_id):
    publicacao = get_object_or_404(Publicacao, id=publicacao_id)
    if request.method == 'POST':
        conteudo = request.POST['conteudo']
        Comentario.objects.create(publicacao=publicacao, autor=request.user, conteudo=conteudo)
        return redirect('lista_publicacoes')
