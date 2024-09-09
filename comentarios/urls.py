# comentarios/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<int:publicacao_id>/comentar/', views.comentar_publicacao, name='comentar_publicacao'),
]
