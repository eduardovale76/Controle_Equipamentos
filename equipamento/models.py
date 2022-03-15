from datetime import date
from django.db import models
from django.conf import settings


class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField()
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    
    
    def __str__(self) -> str:
        return self.nome
    
class Equipamentos(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=30)
    co_autor = models.CharField(max_length=30)
    data_cadastro = models.DateField(default= date.today)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    emprestado = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Equipamento'
        
    def __str__(self):
        return self.nome

class Emprestimos(models.Model):
    nome_emprestado = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, blank=True, null=True)
    nome_emprestado_anonimo = models.CharField(max_length=30, blank=True, null=True)
    data_emprestimo = models.DateField(blank=True, null=True)
    data_devolucao = models.DateField(blank=True, null=True)
    equipamentos = models.ForeignKey(Equipamentos, on_delete=models.DO_NOTHING)
    
  #  class Meta:
   #     verbose_name = 'Emprestimo'
    
    def __str__(self):
        return f'{self.nome_emprestado} | {self.equipamentos}'