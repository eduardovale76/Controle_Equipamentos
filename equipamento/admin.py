from django.contrib import admin
from .models import Empresa, Emprestimos, Equipamentos, Categoria


admin.site.register(Equipamentos)
admin.site.register(Categoria)
admin.site.register(Emprestimos)
admin.site.register(Empresa)