# publicacoes/views.py
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect
from .models import Publicacao
from django.contrib.auth.decorators import login_required

def lista_publicacoes(request):
    publicacoes = Publicacao.objects.all()
    return render(request, 'publicacoes/lista_publicacoes.html', {'publicacoes': publicacoes})

##Método para criação
@login_required
def criar_publicacao(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        descricao = request.POST['descricao']
        foto = request.FILES['foto']
        Publicacao.objects.create(titulo=titulo, descricao=descricao, foto=foto, autor=request.user)
        return redirect('lista_publicacoes')
    return render(request, 'criar_publicacao.html')

def editar_publicacao(request, pk):
    publicacao = get_object_or_404(Publicacao, pk=pk)
    # Verifica se o usuário atual é o autor da publicação
    if request.user != publicacao.autor:
        return HttpResponseForbidden("Você não tem permissão para editar esta publicação.")
    if request.method == 'POST':
        # Atualiza os campos da publicação com os dados recebidos
        publicacao.titulo = request.POST.get('titulo', publicacao.titulo)
        publicacao.descricao = request.POST.get('descricao', publicacao.descricao)
        if 'foto' in request.FILES:
            publicacao.foto = request.FILES['foto']
        publicacao.save()
        return redirect('detalhes_publicacao', pk=publicacao.pk)
    
    return render(request, 'editar_publicacao.html', {'publicacao': publicacao})
def detalhes_publicacao(request, pk):
    publicacao = get_object_or_404(Publicacao, pk=pk)
    return render(request, 'detalhes_publicacao.html', {'publicacao': publicacao})

def curtir_publicacao(request, pk):
    publicacao = get_object_or_404(Publicacao, pk=pk)
    publicacao.curtir()
    return redirect('detalhes_publicacao', pk=pk)

def descurtir_publicacao(request, pk):
    publicacao = get_object_or_404(Publicacao, pk=pk)
    publicacao.descurtir()
    return redirect('detalhes_publicacao', pk=pk)


@login_required
def excluir_publicacao(request, pk):
    publicacao = get_object_or_404(Publicacao, pk=pk)
    
    if publicacao.autor == request.user:
        publicacao.delete()
        return redirect('lista_publicacoes')
    else:
        # Pode redirecionar ou mostrar uma mensagem de erro
        return redirect('lista_publicacoes')