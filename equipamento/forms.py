from django import forms
from .models import Equipamentos

class CadastroEquipamento(forms.ModelForm): 
    class Meta:
        model = Equipamentos
       # fields = ('nome', 'autor', 'co_autor', 'data_cadastro', 'categoria', 'emprestado',)
        exclude = ('usuario',)