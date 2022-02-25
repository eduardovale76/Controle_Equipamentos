from datetime import date
from django.db import models

"""class Emprestimo(models.Model):"""
    



class Equipamentos(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=30)
    co_autor = models.CharField(max_length=30)
    data_cadastro = models.DateField(default= date.today)
    emprestado = models.BooleanField(default=False)
    nome_emprestado = models.CharField(max_length=30, blank=True)
    data_emprestimo = models.DateTimeField(blank=True, null=True)
    data_devolucao = models.DateTimeField(blank=True, null=True)
    tempo_duracao = models.DateField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Equipamento'
        
    def __str__(self):
        return self.nome
    