from django.http import HttpResponse
from django.shortcuts import render, redirect
from usuarios.views import Usuario
from .models import Categoria, Emprestimos, Equipamentos


def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario']) 
        equipamentos = Equipamentos.objects.filter(usuario = usuario)
        return render(request, 'home.html', {'equipamentos': equipamentos})
    else:
        return redirect('/auth/login/?status=2')

def ver_equipamento(request, id):
    if request.session.get('usuario'):
        equipamento = Equipamentos.objects.get(id = id)
        if request.session.get('usuario') == equipamento.usuario.id:
            categoria_equipamento = Categoria.objects.filter(usuario_id = request.session.get('usuario'))
            emprestimos = Emprestimos.objects.filter(equipamentos = equipamento)
            return render(request, 'ver_equipamento.html', {'equipamento':equipamento, 'categoria_equipamento':categoria_equipamento, 'emprestimos': emprestimos})
        else:
            return redirect('/equipamento/home/')
    return redirect('/auth/login/?status=2')