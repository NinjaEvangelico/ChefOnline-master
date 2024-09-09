from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_publicacoes, name='lista_publicacoes'),
    path('criar/', views.criar_publicacao, name='criar_publicacao'),
    path('curtir/<int:pk>/', views.curtir_publicacao, name='curtir_publicacao'),
    path('descurtir/<int:pk>/', views.descurtir_publicacao, name='descurtir_publicacao'),
    path('detalhes/<int:pk>/', views.detalhes_publicacao, name='detalhes_publicacao'),
    path('editar/<int:pk>/', views.editar_publicacao, name='editar_publicacao'),
    path('excluir/<int:pk>', views.excluir_publicacao, name='excluir_publicacao')
]
