from re import search
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
def ver_empresa(request, id):
    empresa = Empresa.objects.get(id = id)
    form = CadastroEmpresa()
    return render(request, 'ver_empresa.html', {'empresa_id':id, 'empresa':empresa, 'form': form})

@login_required
def ver_categoria(request, id):
    categoria = Categoria.objects.get(id = id)
    form = CadastroCategoria()
    return render(request, 'ver_categoria.html', {'id_categoria': id, 'categoria': categoria, 'form':form})


@login_required
def cadastrar_equipamento(request):
    if request.method == "POST":
        form = CadastroEquipamento(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            if not post.imagem:
                post.imagem = 'foto_equipamento/semimg.jpg'
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
def excluir_categoria(request, id):
    Categoria.objects.get(id = id).delete()
    return redirect('/equipamento/listagem_categoria')

@login_required
def excluir_empresa(request, id):
    Empresa.objects.get(id = id).delete()
    return redirect('/equipamento/listagem_empresa')

    
@login_required
def cadastrar_categoria(request):
    if request.method == "POST":
        form = CadastroCategoria(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/equipamento/listagem_categoria')
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
    search_input = request.GET.get('search_area') or ''
    if search_input:
        empresas = Empresa.objects.filter(nome__icontains=search_input)
    return render(request, 'listagem_empresa.html', {'empresas':empresas, 'search_input':search_input})


@login_required
def listagem_categoria(request):
    categorias = Categoria.objects.all()
    search_input = request.GET.get('search_area') or ''
    if search_input:
        categorias = Categoria.objects.filter(nome__icontains=search_input)
    return render(request, 'listagem_categoria.html', {'categorias':categorias, 'search_input':search_input})



@login_required
def listagem_equipamento(request):
    equipamentos = Equipamentos.objects.all()
    search_input = request.GET.get('search_area') or ''
    if search_input:
        equipamentos = Equipamentos.objects.filter(nome__icontains=search_input)
    return render(request, 'listagem_equipamento.html', {'equipamentos':equipamentos, 'search_input':search_input})
        
@login_required
def editar_categoria(request):
    id_categoria = request.POST.get('categoria_id')
    nome = request.POST.get('nome')
    descricao = request.POST.get('descricao')
    categoria = Categoria.objects.get(id = id_categoria)
    categoria.nome = nome
    categoria.descricao = descricao
    categoria.save()
    return redirect('/equipamento/listagem_categoria')
    
        
@login_required       
def editar_equipamento(request):
    #from post
    equipamento_id = request.POST.get('equipamento_id')
    categoria_id = request.POST.get('categoria_id')
    nome = request.POST.get('nome')
    serial = request.POST.get('serial')
    #from table Equipamentos
    equipamento = Equipamentos.objects.get(id = equipamento_id)
    categoria = Categoria.objects.get(id=categoria_id)
    equipamento.categoria = categoria
    equipamento.nome = nome
    equipamento.serial = serial
    equipamento.save()
    #From table Emprestimo
    emprestimo = Emprestimos.objects.filter(equipamentos = equipamento_id)
    return redirect(f'/equipamento/ver_equipamento/{equipamento_id}',{'emprestimo':emprestimo})

@login_required
def editar_empresa(request):
    empresa_id = request.POST.get('empresa_id')
    empresa_nome = request.POST.get('nome')
    empresa_responsavel = request.POST.get('responsavel')
    empresa_email = request.POST.get('email')
    empresa = Empresa.objects.get(id = empresa_id)
    empresa.nome = empresa_nome
    empresa.responsavel = empresa_responsavel
    empresa.email = empresa_email
    empresa.save()
    return redirect('/equipamento/listagem_empresa')


@login_required
def cadastrar_empresa(request):
    if request.method =='POST':
        form = CadastroEmpresa(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.save()
            return redirect('/equipamento/listagem_empresa')
    else:
        form = CadastroEmpresa()
    return render(request, 'cad_empresa.html', {'form':form})

def devolver_equipamento(request):
    equipamento_id = request.POST.get('equipamento_id')
    emprestimos_id = request.POST.get('id')
    emprestimos = get_object_or_404(Emprestimos, id = emprestimos_id)
    emprestimo_defeito = request.POST.get('defeito')
    emprestimo_diagnostico = request.POST.get('diagnostico')
    emprestimo_tecnico = request.POST.get('tecnico_responsavel')
    emprestimo_dt_devolucao = request.POST.get('data_devolucao')
    emprestimos.defeito = emprestimo_defeito
    emprestimos.diagnostico =  emprestimo_diagnostico
    #emprestimos.tecnico_responsavel = emprestimo_tecnico
    emprestimos.data_devolucao = emprestimo_dt_devolucao
    emprestimos.save()
    return redirect(f'/equipamento/ver_equipamento/{equipamento_id}',{'emprestimos':emprestimos})