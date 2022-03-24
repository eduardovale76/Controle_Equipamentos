from django import forms
from .models import Empresa, Equipamentos, Categoria, Emprestimos
from users.models import User

class CadastroEquipamento(forms.ModelForm): 
    class Meta:
        model = Equipamentos
       # fields = ('nome', 'autor', 'co_autor', 'data_cadastro', 'categoria', 'emprestado',)
        exclude = ('usuario',)

class CadastroCategoria(forms.ModelForm): 
    class Meta:
        model = Categoria
      #  fields = '__all__'
        exclude = ('usuario',)

class CadastroEmprestimo(forms.ModelForm):
    class Meta:
        model = Emprestimos
        fields = '__all__'
        
class CadastroUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class CadastroEmpresa(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'
