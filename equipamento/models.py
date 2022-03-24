from datetime import date
from django.db import models
from django.conf import settings


class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField()
    #usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    
    def __str__(self) -> str:
        return self.nome
    
    
class Equipamentos(models.Model):
    nome = models.CharField(max_length=60)
    imagem = models.ImageField(upload_to='foto_equipamento', null=True, blank=True)
    serial = models.CharField(max_length=30)
    empresa = models.CharField(max_length=30)
    data_cadastro = models.DateField(default= date.today)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    #usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    emprestado = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Equipamento'
        
    def __str__(self):
        return self.nome
class Empresa(models.Model):
    nome = models.CharField(max_length=60)
    responsavel = models.CharField(max_length=60)
    
    def __str__(self) -> str:
        return self.nome
    
class Emprestimos(models.Model):
    empresa_responsavel = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING)
    empresa_anonima = models.CharField(max_length=30, blank=True, null=True)
    data_emprestimo = models.DateField(blank=True, null=True)
    data_devolucao = models.DateField(blank=True, null=True)
    equipamentos = models.ForeignKey(Equipamentos, on_delete=models.DO_NOTHING)
    defeito = models.TextField()
    diagnostico = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    tecnico_responsavel = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, blank=True, null=True)
    
    
    
    def __str__(self):
        return f'{self.nome_emprestado} | {self.equipamentos}'
    