from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Categoria, Emprestimos, Equipamentos
from .forms import CadastroCategoria, CadastroEquipamento
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView


def home(request):
    if request.user:
        usuario = request.user.id 
        equipamentos = Equipamentos.objects.filter(usuario = usuario)
        form = CadastroEquipamento()
        #form.fields['nome'].initial = request.session['usuario']
        form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario) #Filtra para os cadastros do usuario
        return render(request, 'home.html', {'equipamentos': equipamentos, 
                                            'usuario_logado': request.user,
                                             'form':form})
  #  else:
   #     return redirect('/auth/login/?status=2')

def ver_equipamento(request, id):
    if request.user:
        equipamento = Equipamentos.objects.get(id = id)
        if request.user.id == equipamento.usuario.id:
            categoria_equipamento = Categoria.objects.filter(usuario_id = request.user.id)
            emprestimos = Emprestimos.objects.filter(equipamentos = equipamento)
            form = CadastroEquipamento()
            usuario =  request.user.id
            form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario) #Filtra para os cadastros do usuario
            return render(request, 'ver_equipamento.html', {'equipamento':equipamento, 
                                                            'categoria_equipamento':categoria_equipamento, 
                                                            'emprestimos': emprestimos, 
                                                            'usuario_logado': request.user, 
                                                            'id_equipamento': id,'form':form})
        else:
            return redirect('/equipamento/home/')
  #  return redirect('/auth/login/?status=2')


def cadastrar_equipamento(request):
    if request.method == 'POST':
        form = CadastroEquipamento(request.POST)
        if form.is_valid():
            form_completo = form.save(commit=False)
            form_completo.usuario = get_user_model()
            form_completo.save()
            return redirect('/equipamento/home/')
        else:
            form = CadastroEquipamento()
            return HttpResponse("Categoria: Dados inválidos")
        
        

def excluir_equipamento(request, id):
    Equipamentos.objects.get(id = id).delete()
    return redirect('/equipamento/home/')
    

class CadastrarCategoria(TemplateView):
    template_name = 'categoria.html'
