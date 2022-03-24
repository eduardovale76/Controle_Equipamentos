from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('ver_equipamento/<int:id>', views.ver_equipamento, name = 'ver_equipamento'), 
    #cadastros
    path('cadastrar_equipamento', views.cadastrar_equipamento, name='cadastrar_equipamento'),
    path('cadastrar_empresa', views.cadastrar_empresa, name='cadastrar_empresa'),
    path('cadastrar_emprestimo', views.cadastrar_emprestimo, name='cadastrar_emprestimo'),
    path('cadastrar_usuario', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('cadastrar_categoria', views.cadastrar_categoria, name='cadastrar_categoria'),
    #edicao
    path('excluir_equipamento/<int:id>', views.excluir_equipamento, name='excluir_equipamento'),
    path('editar_equipamento', views.editar_equipamento, name='editar_equipamento'),
    #listagens
    path('historico_equipamento', views.historico_equipamento, name='historico_equipamento'),
    path('listagem_empresa', views.listagem_empresa, name='listagem_empresa'),
    path('listagem_categoria', views.listagem_categoria, name='listagem_categoria'),
    path('listagem_equipamento', views.listagem_equipamento, name='listagem_equipamento'),
]
