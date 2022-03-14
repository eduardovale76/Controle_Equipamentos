from django import forms
from .models import Equipamentos, Categoria

class CadastroEquipamento(forms.ModelForm): 
    class Meta:
        model = Equipamentos
       # fields = ('nome', 'autor', 'co_autor', 'data_cadastro', 'categoria', 'emprestado',)
        exclude = ('usuario',)

class CadastroCategoria(forms.ModelForm): 
    class Meta:
        model = Categoria
        fields = '__all__'