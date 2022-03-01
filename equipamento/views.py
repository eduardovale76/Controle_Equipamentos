from django.http import HttpResponse
from django.shortcuts import render, redirect
from usuarios.views import Usuario


def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario']).nome
        return HttpResponse(f'Ola, {usuario}')
    else:
        return redirect('/auth/login/?status=2')