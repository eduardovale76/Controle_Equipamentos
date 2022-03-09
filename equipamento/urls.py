from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('ver_equipamento/<int:id>', views.ver_equipamento, name = 'ver_equipamento'), 
    path('cadastrar_equipamento', views.cadastrar_equipamento, name='cadastrar_equipamento'),
]
