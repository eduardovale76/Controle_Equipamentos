from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Categoria, Empresa, Emprestimos, Equipamentos
from .forms import CadastroCategoria, CadastroEquipamento, CadastroEmprestimo, CadastroUser, CadastroEmpresa
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    equipamentos = Equipamentos.objects.all()
    form = CadastroEquipamento()
        #form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario) #Filtra para os cadastros do usuario
    return render(request, 'ver_equipamento_lista.html', {'equipamentos':equipamentos, 'form':form})


@login_required
def ver_equipamento(request, id):
    if request.user:
        equipamento = Equipamentos.objects.get(id = id)
        categoria_equipamento = Categoria.objects.all()
        emprestimos = Emprestimos.objects.filter(equipamentos = equipamento)
        form = CadastroEquipamento()
        return render(request, 'ver_equipamento.html', {'equipamento':equipamento,                       
                                                            'emprestimos':emprestimos,
                                                            'categoria_equipamento':categoria_equipamento,
                                                            'id_equipamento': id,
                                                            'form':form})
    else:
        return redirect('/equipamento/home/')


@login_required
def cadastrar_equipamento(request):
    if request.method == "POST":
        form = CadastroEquipamento(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/equipamento/home/')
    else:
        form = CadastroEquipamento()
    return render(request, 'cad_equipamento.html', {'form':form})
             
@login_required
def excluir_equipamento(request, id):
    Equipamentos.objects.get(id = id).delete()
    return redirect('/equipamento/home/')

    
@login_required
def cadastrar_categoria(request):
    if request.method == "POST":
        form = CadastroCategoria(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/equipamento/home/')
    else:
        form = CadastroCategoria()
    return render(request, 'cad_categoria.html', {'form':form})


@login_required
def cadastrar_emprestimo(request):
    if request.method =="POST":
        form = CadastroEmprestimo(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/equipamento/home/')
    else:
        form = CadastroEmprestimo()
    return render(request, 'cad_emprestimo.html', {'form':form})


@login_required
def cadastrar_usuario(request):
    if request.method =="POST":
        form = CadastroUser(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/equipamento/home/')
    else:
        form = CadastroUser()
    return render(request, 'cad_usuario.html', {'form':form})


@login_required
def historico_equipamento(request):
    emprestimos = Emprestimos.objects.all()
    return render(request, 'historico_equipamento.html', {'emprestimos': emprestimos})


@login_required
def listagem_empresa(request):
    empresas = Empresa.objects.all()
    return render(request, 'listagem_empresa.html', {'empresas':empresas})


@login_required
def listagem_categoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'listagem_categoria.html', {'categorias':categorias})


@login_required
def listagem_equipamento(request):
    equipamentos = Equipamentos.objects.all()
    return render(request, 'listagem_equipamento.html', {'equipamentos':equipamentos})
        
        
@login_required       
def editar_equipamento(request):
    equipamento_id = request.POST.get('equipamento_id')
    categoria_id = request.POST.get('categoria_id')
    nome = request.POST.get('nome')
    autor = request.POST.get('autor')
    co_autor = request.POST.get('co_autor')
    equipamento = Equipamentos.objects.get(id = equipamento_id)
    categoria = Categoria.objects.get(id=categoria_id)
    equipamento.categoria = categoria
    equipamento.nome = nome
    equipamento.autor = autor
    equipamento.co_autor = co_autor
    
    equipamento.save()
    return redirect(f'/equipamento/ver_equipamento/{equipamento_id}')


@login_required
def cadastrar_empresa(request):
    if request.method =='POST':
        form = CadastroEmpresa(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.save()
            return redirect('/equipamento/home/')
    else:
        form = CadastroEmpresa()
    return render(request, 'cad_empresa.html', {'form':form})